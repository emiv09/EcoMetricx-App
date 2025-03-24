from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "38e857fa2a78691fa3da7239805a10b86c946bdcb06d9ecaa2cc54e11001433df98386b82e9b07a3ba700a23391a695b379f7d59e155b38cfa60a6e8cba2bc777d2eeb6a85c3a599d94290c5c1c2e7e754420d25adfadd3d9b55f518d8ee1bae7202a2798101b9b8c4240dab2e17353957c8009383ab000f6b338ce3c7e77331a4c9f6910fd3504cd8d255be89077bf586fbff327c657d569d10c881f3c3336200cdc04263bf4f19c64fedf12bfff5d023ffc5cf7adb5f3226cf6b5f4c8e5e3b4d3e6c775b81f19f86ba9be47eda2d98f37ba6921f489409be504c39e7ae1fdb7adbc150e058f5086620c8c3a1a9a80c4ad539439649e4034e58e86a334cd22b"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()