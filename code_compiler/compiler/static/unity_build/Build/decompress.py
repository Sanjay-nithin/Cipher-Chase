import brotli

with open(r"D:\Cipher-Chase\code_compiler\compiler\static\unity_build\Build\ut-2.framework.js.br", "rb") as file:
    data = file.read()

decompressed_data = brotli.decompress(data)

with open(r"D:\Cipher-Chase\code_compiler\compiler\static\unity_build\Build\ut-2.framework.js", "wb") as f:
    f.write(decompressed_data)

print("Decompression complete: ut-2.framework.js")