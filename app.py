import os
from openai import OpenAI

# ==========================================
# 0. 基础配置 (系统初始化)
# ==========================================
# 这里默认使用 OpenAI 接口标准。
# 如果你申请时填写的是其他模型（如 DeepSeek/GLM），只需替换 base_url 和 api_key 即可。
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "你的API_KEY_填在这里"),
    base_url="https://api.openai.com/v1" # 若使用国内代理或其他兼容API，请修改此处
)

MODEL_NAME = "gpt-4-turbo" # 对应你在表单中勾选的 GPT 系列

def run_agent(role_prompt, user_prompt):
    """通用 Agent 执行引擎"""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": role_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Agent 运行出错: {str(e)}"

# ==========================================
# 1. 核心业务逻辑：多 Agent 协作工作流
# ==========================================
def automated_ops_workflow(topic):
    print(f"🚀 [系统启动] 协同运营自动化系统\n🎯 今日执行主题：{topic}\n" + "-"*40)

    # Agent 1: 趋势嗅探员 (长链推理，分析痛点)
    print("🕵️ [Agent 1] 趋势嗅探员正在分析市场数据...")
    research_prompt = "你是一个资深的行业数据分析师。请分析给定主题的最新市场趋势，并总结出受众的3个核心痛点。要求逻辑严密，条理清晰。"
    research_report = run_agent(research_prompt, f"分析主题：{topic}")
    print(f"✅ [Agent 1 完成] 产出报告摘要:\n{research_report[:100]}...\n" + "-"*40)

    # Agent 2: 内容创作者 (基于上游数据生成内容)
    print("✍️ [Agent 2] 内容创作者正在根据报告撰写文案...")
    writer_prompt = "你是一个爆款内容制造机。请根据上游提供的分析报告，写一篇面向年轻用户的社交媒体推广文案。要求：吸引眼球，适当使用emoji。"
    draft_content = run_agent(writer_prompt, f"请参考以下报告进行创作：\n{research_report}")
    print(f"✅ [Agent 2 完成] 产出初稿摘要:\n{draft_content[:100]}...\n" + "-"*40)

    # Agent 3: 审核主编 (质量把控与最终合规)
    print("⚖️ [Agent 3] 审核主编正在进行终审和润色...")
    reviewer_prompt = "你是一个严格的品牌审核主编。请检查提供的初稿文案，确保没有违禁词，语句通顺，并给出最终可以直接复制发布的排版版本。"
    final_publish_content = run_agent(reviewer_prompt, f"请审核以下初稿：\n{draft_content}")
    
    return final_publish_content

# ==========================================
# 2. 启动入口
# ==========================================
if __name__ == "__main__":
    # 测试运行
    test_topic = "AI大模型如何改变程序员的日常开发"
    
    final_result = automated_ops_workflow(test_topic)
    
    print("\n🎉 [工作流结束] 最终审核通过的发布内容如下：\n")
    print("="*50)
    print(final_result)
    print("="*50)