{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65e271ce-53c8-41f5-9e1c-89e9f083cecd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  hello\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Bot: Hello. How can I assist you today? Do you have any questions about Python or any other programming-related topic?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Bot: We can just chat if you'd like. I'm here to help if you have any questions or need assistance in the future.\n",
      "\n",
      "If you do happen to think of something, feel free to ask me anytime. Otherwise, I'll just be here. Would you like to learn something new about Python?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  exit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Bot: Goodbye.\n"
     ]
    }
   ],
   "source": [
    "from groq import Groq\n",
    "client = Groq(\n",
    "    api_key=\"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\"\n",
    ")\n",
    "messages = [\n",
    "    {\n",
    "        \"role\": \"system\",\n",
    "        \"content\": \"You are a helpful Python doubt solver. Explain concepts in simple language with examples.\"\n",
    "    }\n",
    "]\n",
    "for i in range(4):\n",
    "\n",
    "    user_input = input(\"You: \")\n",
    "    messages.append(\n",
    "        {\n",
    "            \"role\": \"user\",\n",
    "            \"content\": user_input\n",
    "        }\n",
    "    )\n",
    "    response = client.chat.completions.create(\n",
    "        model=\"llama-3.1-8b-instant\",\n",
    "        messages=messages,\n",
    "        temperature=0.7\n",
    "    )\n",
    "    reply = response.choices[0].message.content\n",
    "    print(\"\\nBot:\", reply)\n",
    "    messages.append(\n",
    "        {\n",
    "            \"role\": \"assistant\",\n",
    "            \"content\": reply\n",
    "        }\n",
    "    )\n",
    "\n",
    "print(\"\\n\\nFULL MESSAGE HISTORY\\n\")\n",
    "\n",
    "for msg in messages:\n",
    "    print(f\"{msg['role'].upper()}: {msg['content']}\")\n",
    "    print(\"-\" * 50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "077747a6-ec74-4432-9e5f-8c99f42ee162",
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
