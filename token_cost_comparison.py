{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29c9287f-b09d-4dd7-8db0-39c1cdbf7883",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tiktoken\n",
    "import pandas as pd\n",
    "encoding = tiktoken.get_encoding(\"cl100k_base\")\n",
    "def token_cost(text, price_per_million=0.10):\n",
    "    tokens = encoding.encode(text)\n",
    "    token_count = len(tokens)\n",
    "    cost = (token_count / 1_000_000) * price_per_million\n",
    "    \n",
    "    return token_count, cost\n",
    "paragraph = \"Artificial Intelligence is transforming industries and improving daily life. \" * 30\n",
    "\n",
    "python_script = \"\"\n",
    "\n",
    "for i in range(50):\n",
    "    python_script += f\"print('This is line {i+1}')\\n\"\n",
    "\n",
    "conversation = \"\"\"\n",
    "User: Hello, how are you?\n",
    "Assistant: I am doing well. How can I help you today?\n",
    "\n",
    "User: Explain machine learning in simple terms.\n",
    "Assistant: Machine learning is a method where computers learn patterns from data.\n",
    "\n",
    "User: Give me an example.\n",
    "Assistant: Spam email filtering is a common example of machine learning.\n",
    "\"\"\"\n",
    "results = []\n",
    "\n",
    "for name, text in [\n",
    "    (\"300-word Paragraph\", paragraph),\n",
    "    (\"50-line Python Script\", python_script),\n",
    "    (\"3-turn Conversation\", conversation)\n",
    "]:\n",
    "    tokens, cost = token_cost(text)\n",
    "\n",
    "    results.append({\n",
    "        \"Input Type\": name,\n",
    "        \"Token Count\": tokens,\n",
    "        \"Estimated Cost ($)\": round(cost, 8)\n",
    "    })\n",
    "\n",
    "df = pd.DataFrame(results)\n",
    "print(\"\\nTOKEN COST COMPARISON TABLE\\n\")\n",
    "print(df.to_string(index=False))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
