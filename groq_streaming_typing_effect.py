{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9bbbb03-78d0-462a-8b94-5b5a01c5ba69",
   "metadata": {},
   "outputs": [],
   "source": [
    "from groq import Groq\n",
    "import time\n",
    "client = Groq(\n",
    "    api_key=\"YOUR_GROQ_API_KEY\"\n",
    ")\n",
    "prompt = \"Write a short 4-line poem about the moon.\"\n",
    "\n",
    "print(\"\\nGenerating poem with typing effect...\\n\")\n",
    "\n",
    "stream = client.chat.completions.create(\n",
    "    model=\"llama-3.1-8b-instant\",\n",
    "    messages=[\n",
    "        {\n",
    "            \"role\": \"user\",\n",
    "            \"content\": prompt\n",
    "        }\n",
    "    ],\n",
    "    temperature=0.7,\n",
    "    stream=True\n",
    ")\n",
    "tokens_list = []\n",
    "start_time = time.time()\n",
    "for chunk in stream:\n",
    "\n",
    "    token = chunk.choices[0].delta.content\n",
    "\n",
    "    if token:\n",
    "        print(token, end=\"\", flush=True)\n",
    "        tokens_list.append(token)\n",
    "        time.sleep(0.02)\n",
    "end_time = time.time()\n",
    "final_text = \"\".join(tokens_list)\n",
    "total_tokens = len(tokens_list)\n",
    "generation_time = end_time - start_time\n",
    "tokens_per_second = total_tokens / generation_time\n",
    "\n",
    "print(\"\\n\\n\" + \"=\"*50)\n",
    "print(\"PERFORMANCE REPORT\")\n",
    "print(\"=\"*50)\n",
    "\n",
    "print(f\"Total Tokens Received : {total_tokens}\")\n",
    "print(f\"Generation Time       : {generation_time:.2f} seconds\")\n",
    "print(f\"Tokens Per Second     : {tokens_per_second:.2f}\")\n",
    "print(\"\\nFinal Generated Text:\\n\")\n",
    "print(final_text)"
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
