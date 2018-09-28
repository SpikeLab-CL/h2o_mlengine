import subprocess
import os
import sys

def download_file_from_storage(gs_file_path):
    """download a file from GCS into ml-engine running container
        Arguments:
            gs_ile_path: string path to the MOJO file.
        Returns:
            string: path of the downloaded file
    """
    file_name = "{0}".format(gs_file_path.split("/")[-1])
    subprocess.check_call(['gsutil','-q', 'cp', gs_file_path, file_name], stderr=sys.stdout)
    path = "{0}/{1}".format(os.getcwd(),file_name)
    return path

def save_in_gcs(file_path, gcs_path):
    """Store a file into GCS
        Arguments:
            file_path: string with the file path.
            gcs_path: string path to the GCS folder
    """
    subprocess.check_call(['gsutil','-q', 'cp', file_path, gcs_path], stderr=sys.stdout)