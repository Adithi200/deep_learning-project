{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "88db3098-c0d3-497b-aa03-bd0e7ad1ad1a",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tiktoken'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mtiktoken\u001b[39;00m\n\u001b[32m      2\u001b[39m encoding = tiktoken.get_encoding(\u001b[33m\"\u001b[39m\u001b[33mcl100k_base\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      3\u001b[39m inputs = {\n\u001b[32m      4\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mEnglish Sentence\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mArtificial Intelligence is changing the world.\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m      5\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mPython Function\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\"\"\u001b[39m\n\u001b[32m   (...)\u001b[39m\u001b[32m     12\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mMath Notation\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mf(x) = x^2 + 3x - 5\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m     13\u001b[39m }\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'tiktoken'"
     ]
    }
   ],
   "source": [
    "import tiktoken\n",
    "encoding = tiktoken.get_encoding(\"cl100k_base\")\n",
    "inputs = {\n",
    "    \"English Sentence\": \"Artificial Intelligence is changing the world.\",\n",
    "    \"Python Function\": \"\"\"\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "\"\"\", \n",
    "    \"Native Language Sentence\": \"എനിക്ക് പ്രോഗ്രാമിംഗ് പഠിക്കാൻ ഇഷ്ടമാണ്\",\n",
    "    \"Number\": \"1234567\",\n",
    "    \"Email Address\": \"student123@gmail.com\",\n",
    "    \"Math Notation\": \"f(x) = x^2 + 3x - 5\"\n",
    "}\n",
    "for name, text in inputs.items():\n",
    "    tokens = encoding.encode(text)\n",
    "    token_strings = [encoding.decode([token]) for token in tokens]\n",
    "    print(f\"\\n{name}\")\n",
    "    print(\"-\" * 40)\n",
    "    print(\"Input:\", text)\n",
    "    print(\"Tokens:\", token_strings)\n",
    "    print(\"Token Count:\", len(tokens))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bcf0e454-d399-4a77-9a16-6f5c615fe74b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting tiktoken\n",
      "  Downloading tiktoken-0.13.0-cp313-cp313-win_amd64.whl.metadata (6.8 kB)\n",
      "Requirement already satisfied: regex in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from tiktoken) (2025.9.1)\n",
      "Requirement already satisfied: requests in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from tiktoken) (2.32.5)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from requests->tiktoken) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from requests->tiktoken) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from requests->tiktoken) (2.5.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from requests->tiktoken) (2026.4.22)\n",
      "Downloading tiktoken-0.13.0-cp313-cp313-win_amd64.whl (874 kB)\n",
      "   ---------------------------------------- 0.0/874.8 kB ? eta -:--:--\n",
      "   ----------- ---------------------------- 262.1/874.8 kB ? eta -:--:--\n",
      "   ---------------------------------------- 874.8/874.8 kB 4.5 MB/s  0:00:00\n",
      "Installing collected packages: tiktoken\n",
      "Successfully installed tiktoken-0.13.0\n"
     ]
    }
   ],
   "source": [
    "!pip install tiktoken\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fb968e44-05c4-4001-8053-5694028008f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "English Sentence\n",
      "----------------------------------------\n",
      "Input: Artificial Intelligence is changing the world.\n",
      "Tokens: ['Art', 'ificial', ' Intelligence', ' is', ' changing', ' the', ' world', '.']\n",
      "Token Count: 8\n",
      "\n",
      "Python Function\n",
      "----------------------------------------\n",
      "Input: \n",
      "def add(a, b):\n",
      "    return a + b\n",
      "\n",
      "Tokens: ['\\n', 'def', ' add', '(a', ',', ' b', '):\\n', '   ', ' return', ' a', ' +', ' b', '\\n']\n",
      "Token Count: 13\n",
      "\n",
      "Native Language Sentence\n",
      "----------------------------------------\n",
      "Input: എനിക്ക് പ്രോഗ്രാമിംഗ് പഠിക്കാൻ ഇഷ്ടമാണ്\n",
      "Tokens: ['�', '�', '�', '�', '�', '�', '�', '�', '്�', '�', '്', ' �', '�', '�', '്�', '�', '�', '�', '�', '�', '്�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '്', ' �', '�', '�', '�', '�', '�', '�', '�', '�', '്�', '�', '�', '�', '�', '�', ' �', '�', '�', '�', '�', '്�', '�', '�', '�', '�', '�', '�', '�', '്']\n",
      "Token Count: 62\n",
      "\n",
      "Number\n",
      "----------------------------------------\n",
      "Input: 1234567\n",
      "Tokens: ['123', '456', '7']\n",
      "Token Count: 3\n",
      "\n",
      "Email Address\n",
      "----------------------------------------\n",
      "Input: student123@gmail.com\n",
      "Tokens: ['student', '123', '@gmail', '.com']\n",
      "Token Count: 4\n",
      "\n",
      "Math Notation\n",
      "----------------------------------------\n",
      "Input: f(x) = x^2 + 3x - 5\n",
      "Tokens: ['f', '(x', ')', ' =', ' x', '^', '2', ' +', ' ', '3', 'x', ' -', ' ', '5']\n",
      "Token Count: 14\n"
     ]
    }
   ],
   "source": [
    "import tiktoken\n",
    "encoding = tiktoken.get_encoding(\"cl100k_base\")\n",
    "inputs = {\n",
    "    \"English Sentence\": \"Artificial Intelligence is changing the world.\",\n",
    "    \"Python Function\": \"\"\"\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "\"\"\", \n",
    "    \"Native Language Sentence\": \"എനിക്ക് പ്രോഗ്രാമിംഗ് പഠിക്കാൻ ഇഷ്ടമാണ്\",\n",
    "    \"Number\": \"1234567\",\n",
    "    \"Email Address\": \"student123@gmail.com\",\n",
    "    \"Math Notation\": \"f(x) = x^2 + 3x - 5\"\n",
    "}\n",
    "for name, text in inputs.items():\n",
    "    tokens = encoding.encode(text)\n",
    "    token_strings = [encoding.decode([token]) for token in tokens]\n",
    "    print(f\"\\n{name}\")\n",
    "    print(\"-\" * 40)\n",
    "    print(\"Input:\", text)\n",
    "    print(\"Tokens:\", token_strings)\n",
    "    print(\"Token Count:\", len(tokens))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9fe28d1-a735-4454-a2f1-90f56d67a87c",
   "metadata": {},
   "outputs": [],
   "source": []
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
