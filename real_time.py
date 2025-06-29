# from serpapi import GoogleSearch
# import google.generativeai as genai
# genai.configure(api_key="AIzaSyA_ylfWr7QGgqeEFK3ef68uf63UBFkwdfE")

# model = genai.GenerativeModel('gemini-2.0-flash')
# params = {
#     "q":"Python programming",
#     "hl":"en",
#     "gl":"us",
#     "api_key":"c634aa28af68a7b1132ad020fa7de5e50fa7311dec9e1b4c3f3c457197059c44"
# }
# def google_search(query):
#     params = {
#     "q":query,
#     "hl":"en",
#     "gl":"us",
#     "api_key":"c634aa28af68a7b1132ad020fa7de5e50fa7311dec9e1b4c3f3c457197059c44"
#     }
#     search = GoogleSearch(params)
#     results = search.get_dict()
#     # for result in results.get("organic_results", []):
#     #     print(f"Title: {result.get('title')}")
#     #     print(f"Link: {result.get('link')}")
#     #     print(f"snippet: {result.get('snippet')}")
#     if "organic_results" in  results:
#         return "\n".join([res['snippet']for res in results["organic_results"][:5]])
#     else:
#         return "No results found."


# # 
# # print(google_search("Python programming"))

# def chat_with_ai(query):
#     search_result = google_search(query)
#     prompt = f""" i searched google for {query} and got this result: {search_result}.
#     based on this give me a concise and to the point answer to my query."""
#     response = model.generate_content(prompt)
#     return response.text

# print(chat_with_ai("what is current price of bitcoin?"))


