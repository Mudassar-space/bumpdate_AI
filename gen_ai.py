# import google.generativeai as genai
# genai.configure(api_key="AIzaSyA_ylfWr7QGgqeEFK3ef68uf63UBFkwdfE")

# model = genai.GenerativeModel('gemini-2.0-flash')

# # memory=  []

# # while True:
# #     q = input("You: ")
# #     memory.append(f"User: {q}")
# #     prompt = "\n".join(memory) + "\nAI:"
# #     response = model.generate_content(prompt)
# #     memory.append(f"AI: {response.text}")
# #     # print(f"AI: {response.text}")
# #     if q.lower() == 'exit':
# #         break
# #     response = model.generate_content(q)
# #     print(f"AI: {response.text}")

# # print(memory)






# import google.generativeai as genai

# # ✅ Configure API key
# genai.configure(api_key="AIzaSyA_ylfWr7QGgqeEFK3ef68uf63UBFkwdfE")

# # ✅ Load Gemini model
# model = genai.GenerativeModel('gemini-2.0-flash')
#   # or 'gemini-2.0-pro' if available

# # ✅ Store conversation memory
# memory = []

# print("🤖 Gemini Mom Friend is here! (Type 'exit' to quit)\n")

# while True:
#     # Get user input
#     user_input = input("You: ")
    
#     if user_input.lower().strip() == "exit":
#         print("👋 Goodbye!")
#         break

#     # Add user message to memory
#     memory.append(f"User: {user_input}")

#     # Build prompt from memory
#     prompt = (
#         "You are a supportive, loving, slightly humorous 'Mom Friend' for a pregnant woman. "
#         "You talk like a real mom would — warm, honest, and emotionally supportive. "
#         "Keep your answers short, sweet, and helpful.\n\n"
#         + "\n".join(memory) +
#         "\nAI:"
#     )

#     # Get AI response
#     response = model.generate_content(prompt)
#     ai_reply = response.text.strip()

#     # Add AI reply to memory
#     memory.append(f"AI: {ai_reply}")

#     # Show reply
#     print(f"Mom Friend: {ai_reply}")
