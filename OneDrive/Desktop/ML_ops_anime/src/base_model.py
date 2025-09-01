from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dot, Flatten, Dense, Activation, BatchNormalization
from utils.common_functions import read_yaml
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)


class BaseModel:
    def __init__(self, config_path):
        try:
            self.config = read_yaml(config_path)
            logger.info("Loaded configuration from config.yaml")
        except Exception as e:
            raise CustomException("Error loading confguration jackoff!", e)
        
    def RecommenderNet(self, n_users, n_anime):
         
         try:

            embedding_size = self.config["mode;"]["embedding_size"]

            user = Input(name="user", shape= [1])
            user_embedding = Embedding(name="user_embedding", input_dim=n_users, output_dim=embedding_size)(user)

            anime = Input(name="anime", shape=[1])

            anime_embedding = Embedding(name="anime_embedding", input_dim=n_anime, output_dim=embedding_size)(anime)

            X = Dot(name="dot_product", normalize=True,axes=2)([user_embedding,anime_embedding])

            X = Flatten()(X)
        
            X = Dense(1, kernal_initializer="he_normal")(X)
            X = BatchNormalization()(X)
            X = Activation("sigmoid")(X)

            model= Model(inputs=[user,anime],output=X)
            model.compile(
                loss = self.config["model"]["loss"],
                optimizer = self.config["model"]["optimizer"],
                metrics = self.config["model"]["metrics"]

            )
            logger.info("Model creatrd successfully")
            return model
         except Exception as e:
            logger.errir(f"Error occured during model architecture. {e}")
            raise CustomException("Failed to create model 'bonehead'", e)
         





   