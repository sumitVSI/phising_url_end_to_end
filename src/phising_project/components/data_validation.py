import os
import pandas as pd
import numpy as np
from phising_project.logging import logger
from phising_project.constants import *
from phising_project.utils.common import *
from phising_project.entity import DataIngestionConfiguration,DataValidationConfiguration
from phising_project.config.configuration import ConfigurationManager

class DataValidation:
    
    def __init__(self,
                 ingestion_config:DataIngestionConfiguration,
                 config:DataValidationConfiguration):
        try:
            self.ingestion_config = ingestion_config
            self.config = config
            self.validation_status_file_name = os.path.join(self.config.status_file_path,VALIDATION_STATUS_FILE_NAME)

            # self.non_malicious_file_data = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,NON_MALICIOUS_URL_FILE_NAME))
            # self.malicious_file_data = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,MALICIOUS_URL_FILE_NAME))

            cfgm = ConfigurationManager()
            self.schema = cfgm.schema
            self.non_feature_column = self.schema.NON_FEATURE_COLUMN
            self.feature_columns = self.schema.FEATURE_COLUMNS
            self.target_column = self.schema.TARGET_COLUMN
            self.total_columns = list(self.non_feature_column.keys()) + list(self.feature_columns.keys()) + list(self.target_column.keys())

        except Exception as e:
            raise e

    def file_exist_validation(self):
        try:
            require_file_status = None
            
            all_files = os.listdir(self.ingestion_config.unzip_data_path)
    
            with open(self.validation_status_file_name,"w") as f:
                f.write(f">>>>>>>>>>>>>>>>>>>>>>>file exist validation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
                if (MALICIOUS_URL_FILE_NAME in all_files) and (NON_MALICIOUS_URL_FILE_NAME in all_files):  
                    require_file_status = True
                    f.write(f"validation status : {require_file_status} ----------------> {MALICIOUS_URL_FILE_NAME} and {NON_MALICIOUS_URL_FILE_NAME} are present\n\n")
                else:
                    require_file_status = False
                    f.write(f"validation status : {require_file_status} ----------------> require file for training are not present\n\n")
            
            f.close()

            if not require_file_status:
                logger.info("file exist validation failed")
                sys.exit(1)
            else:
                # non_malicious_file_data = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,NON_MALICIOUS_URL_FILE_NAME))
                # malicious_file_data = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,MALICIOUS_URL_FILE_NAME))
                logger.info(f"Validation status updated in : {self.validation_status_file_name} ---> file exist validation completed ")
            
        except Exception as e:
            raise e
        
    def number_of_columns_validation(self):
        try:
            number_of_column_status = None

            non_malicious_file = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,NON_MALICIOUS_URL_FILE_NAME))
            malicious_file = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,MALICIOUS_URL_FILE_NAME))

            total_columns = set(self.total_columns)
            malicious_columns = set(malicious_file.columns)
            non_malicious_columns = set(non_malicious_file.columns)

            with open(self.validation_status_file_name,"a") as f:
                f.write(f">>>>>>>>>>>>>>>>>>>>>>>number of column validation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
                if len(total_columns)==len(malicious_columns)==len(non_malicious_columns):
                    number_of_column_status = True
                    f.write(f"validation status : {number_of_column_status} ----------------> total number of columns are : {len(total_columns)}\n\n")
                else:
                    number_of_column_status = False
                    f.write(f"validation status : {number_of_column_status} ----------------> num_of_schema_column:{len(total_columns)},num_of_malicious_column:{len(malicious_columns)},num_of_nonmalicious_column:{len(non_malicious_columns)}\n\n")
                    
                if number_of_column_status:
                    column_match_status = True
                    for clm in total_columns:
                        if (clm not in malicious_columns) or (clm not in non_malicious_columns):
                            column_match_status = False
                            f.write(f"validation status : {column_match_status} ----------------> {clm} not in train files\n\n")
                            logger.info("feature match status failed")
                            sys.exit(1)
                            break
                if column_match_status:
                        
                        f.write(f"validation status : {column_match_status} ----------------> all features present in train files\n\n")

                else:
                    logger.info("number of column validation failed")

            f.close()
            logger.info(f"Validation status updated in : {self.validation_status_file_name} ---> number of columns validation completed")    
                    
        except Exception as e:
            raise e
        
    def datatype_of_columns_validation(self):

        try:
            datatype_validation_nfc = None ## nfc = non feature column
            datatype_validation_fc = None ## fc = feature column
            datatype_validation_tc = None ## tc = target column

            non_malicious_file = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,NON_MALICIOUS_URL_FILE_NAME))
            malicious_file = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,MALICIOUS_URL_FILE_NAME))

            with open(self.validation_status_file_name,"a") as f:
                f.write(f">>>>>>>>>>>>>>>>>>>>>>>data type of column validation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
                for clm in self.non_feature_column.keys():
                    if (malicious_file[clm].dtype == self.non_feature_column[clm]) and (non_malicious_file[clm].dtype == self.non_feature_column[clm]):
                        datatype_validation_nfc = True
                        f.write(f"validation status: {datatype_validation_nfc}------->The {clm} is present in training files\n\n")
                    else:
                        datatype_validation_nfc = False
                        f.write(f"validation status: {datatype_validation_nfc}------->The {clm} has not in specified data type: {self.non_feature_column[clm]}\n\n")

                for clm in self.feature_columns.keys():
                    if (malicious_file[clm].dtype == self.feature_columns[clm]) and (non_malicious_file[clm].dtype == self.feature_columns[clm]):
                        datatype_validation_fc = True
                        f.write(f"validation status: {datatype_validation_fc}------->The {clm} is present in training files has data type: {self.feature_columns[clm]}\n\n")
                    else:
                        datatype_validation_fc = False
                        f.write(f"validation status: {datatype_validation_fc}------->The {clm} has not in specified data type: {self.feature_columns[clm]}\n\n")
                        logger.info(f"Data Type of feature column validation status failed : {clm} ---> {self.feature_columns[clm]}")
                        sys.exit(1)

                if datatype_validation_fc:
                    for clm in self.target_column.keys():
                        if (malicious_file[clm].dtype == self.target_column[clm]) and (non_malicious_file[clm].dtype == self.target_column[clm]):
                            datatype_validation_tc = True
                            f.write(f"validation status: {datatype_validation_tc}------->The target {clm} is present in training files has data type: {self.target_column[clm]}\n\n")
                        else:
                            datatype_validation_tc = False
                            f.write(f"validation status: {datatype_validation_tc}------->The target {clm} has not in specified data type: {self.target_column[clm]}\n\n")
                            logger.info(f"Data Type of target column validation status failed : {clm} ---> {self.target_column[clm]}")
                            sys.exit(1)
            
            f.close()
            logger.info(f"Validation status updated in : {self.validation_status_file_name} ---> datatype of columns validation completed ")

        except Exception as e:
            raise e
        
    def null_value_of_columns_validation(self):
        try:
            null_value_validation_status = None

            non_malicious_file = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,NON_MALICIOUS_URL_FILE_NAME))
            malicious_file = pd.read_csv(os.path.join(self.ingestion_config.unzip_data_path,MALICIOUS_URL_FILE_NAME))
            
            malicious_null_status = int(malicious_file.isna().sum().sum())
            non_malicious_null_status = int(non_malicious_file.isna().sum().sum())
            with open(self.validation_status_file_name,"a") as f:
                f.write(f">>>>>>>>>>>>>>>>>>>>>>>null value of column validation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
                if malicious_null_status==non_malicious_null_status==0:
                    null_value_validation_status = True
                    f.write(f"validation status : {null_value_validation_status} -----> No null value present in training files\n\n")
                elif malicious_null_status!=0:
                    null_value_validation_status = False
                    null_features_malicious_file = [feature for feature in malicious_file.columns if malicious_file[feature].isna().sum()>0]
                    f.write(f"validation status : {null_value_validation_status} -----> null value present in malicious url training data : {null_features_malicious_file}\n\n")
                elif non_malicious_null_status!=0:
                    null_value_validation_status = False
                    null_features_non_malicious_file = [feature for feature in non_malicious_file.columns if non_malicious_file[feature].isna().sum()>0]
                    f.write(f"validation status : {null_value_validation_status} -----> null value present in malicious url training data : {null_features_non_malicious_file}\n\n")

            
                logger.info(f"Validation status updated in : {self.validation_status_file_name} ---> null value of columns validation completed")
                f.write(f">>>>>>>>>>>>>>>>>>>>>>>training file save in valid location<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
                if null_value_validation_status:
                    malicious_file.to_csv(os.path.join(self.config.validate_data_path,MALICIOUS_URL_FILE_NAME),index=False)
                    non_malicious_file.to_csv(os.path.join(self.config.validate_data_path,NON_MALICIOUS_URL_FILE_NAME),index=False)
                    f.write(f"validation status : training file saved in : {self.config.validate_data_path}\n\n")
                    logger.info(f"Validated file saved in : {self.config.validate_data_path} ")
                else:
                    malicious_file.dropna(inplace=True)
                    malicious_file.reset_index(drop=True,inplace=True)
                    non_malicious_file.dropna(inplace=True)
                    non_malicious_file.reset_index(drop=True,inplace=True)
                    malicious_file.to_csv(os.path.join(self.config.validate_data_path,MALICIOUS_URL_FILE_NAME),index=False)
                    non_malicious_file.to_csv(os.path.join(self.config.validate_data_path,NON_MALICIOUS_URL_FILE_NAME),index=False)
                    f.write(f"validation status : training file saved after dropping null values : {self.config.validate_data_path}\n\n")
                    logger.info(f"Validated file saved after dropping null values : {self.config.validate_data_path} ")
            f.close()

        except Exception as e:
            raise e   