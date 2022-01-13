from LZW import LZW
import os

inputFile = input("Input file name : ")
compressor = LZW(os.path.join("Images",inputFile))
compressor.compress()


compressedFile = input("Compressed file name : ")
decompressor = LZW(os.path.join("CompressedFiles",compressedFile))
decompressor.decompress()