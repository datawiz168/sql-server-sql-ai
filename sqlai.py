# 导入openai库
import openai

# 设置你的OpenAI API密钥
openai.api_key = ''

# 定义一个函数来优化SQL查询
def optimize_sql(query):
    # 使用OpenAI的API，提交原始的SQL查询，请求模型提供一个优化版本
    response = openai.Completion.create(
      engine="text-davinci-003",  # 使用davinci-003引擎
      prompt=f"Optimize the following SQL query: {query}",  # 提示语，告诉模型我们想要优化的查询
      max_tokens=150  # 输出的最大长度
    )
    # 从API响应中提取优化后的查询
    optimized_query = response.choices[0].text.strip()
    return optimized_query

# 使用上述函数
query = "SELECT * FROM users WHERE age > 18"
optimized_query = optimize_sql(query)
print(f"Original Query: {query}")
print(f"Optimized Query: {optimized_query}")

# 输出可能如下：
# Original Query: SELECT * FROM users WHERE age > 18
# Optimized Query: SELECT column1, column2, column3 FROM users WHERE age > 18
# 其中，column1, column2, column3是users表中的列名。这只是一个示例，实际的列名可能会有所不同。

# 注意：
# - 确保您已经安装了openai库，并且有一个有效的OpenAI API密钥。
# - 上述代码仅供示例，实际效果可能因查询和OpenAI模型版本而异。
# - 您可以根据需要调整max_tokens的值，以获取更长或更短的输出。
