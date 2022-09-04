import sys
import io


from BOJ._1920 import problem


file = open("inputs.txt", "w")
# 다음 데이터에 그대로 여러 데이터를 복사붙여넣기 하면 됨
data = """5
4 1 5 2 3
5
1 3 7 9 5
"""
file.write(data)
file.close()
input_file = open("inputs.txt", "r")
sys.stdin = io.StringIO(input_file.read())


problem()
