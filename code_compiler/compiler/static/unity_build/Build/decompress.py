import brotli

with open(r"D:\Game\code_compiler\compiler\static\unity_build\Build\created-games-unity.framework.js.br", "rb") as f:
    c_d = f.read()
decompressed = brotli.decompress(c_d)

with open(r"D:\Game\code_compiler\compiler\static\unity_build\Build\created-games-unity.framework.js", "wb") as f:
    f.write(decompressed)