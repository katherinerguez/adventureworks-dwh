from typing import Any
from abc import ABC, abstractmethod
from dagster_pyspark import PySparkResource
from dagster import ConfigurableResource, ResourceDependency, EnvVar
from pyspark.sql import DataFrame
from pydantic import Field
import os

import requests
import tempfile

class HTTPCSVResource(ConfigurableResource, ABC):
    """
    Clase base abstracta para un recurso que lee archivos CSV desde un endpoint HTTP.
    """
    host: str = Field(description="El hostname del servidor de archivos.")
    port: str = Field(description="El puerto del servidor de archivos.")
    
    @abstractmethod
    def fetch_csv(self, file_name: str) -> Any:
       pass

    def _build_url(self, file_name: str) -> str:
        """Construye la URL completa para un archivo dado."""
        return f"http://{self.host}:{self.port}/data/{file_name}"
 

class PySparkHTTPCSVResource(HTTPCSVResource):
    """
    Para leer un CSV desde una URL HTTP.
    """
    pyspark: ResourceDependency[PySparkResource]

    def fetch_csv(self, file_name: str) -> DataFrame:

        url = self._build_url(file_name)

        temp_dir = tempfile.mkdtemp()

        local_file_path = os.path.join(temp_dir, file_name)
        
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()  
                with open(local_file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        except requests.exceptions.RequestException as e:

            os.remove(local_file_path)
            os.rmdir(temp_dir)
            raise ConnectionError(f"No se pudo descargar el archivo desde {url}. Error: {e}")

        df = self.pyspark.spark_session.read.csv(
            path=local_file_path,
            header=True,
            inferSchema=True
        )
        return df