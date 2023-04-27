from fastapi import FastAPI
##from Symetric import *

pythonApi = FastAPI()

@pythonApi.get("/symetric/key")
async def root():
    return ##getSymrtricKey()

@pythonApi.post("/symetric/key")
async def say_hello(name: str):
    return

@pythonApi.post("/symetric/encode")
async def root():
    return

@pythonApi.post("/symetric/decode")
async def say_hello(name: str):
    return

@pythonApi.get("/symetric/key")
async def root():
    return

@pythonApi.post("/symetric/key")
async def say_hello(name: str):
    return

############## ASYMETRIC #########################

@pythonApi.get("/asymetric/key")
async def say_hello(name: str):
    return

@pythonApi.get("/asymetric/key/ssh")
async def root():
    return

@pythonApi.post("/asymetric/key")
async def say_hello(name: str):
    return

@pythonApi.get("/asymetric/verify")
async def root():
    return

@pythonApi.post("/asymetric/sign")
async def say_hello(name: str):
    return

@pythonApi.get("/asymetric/encode")
async def root():
    return

@pythonApi.post("/asymetric/decode")
async def say_hello(name: str):
    return