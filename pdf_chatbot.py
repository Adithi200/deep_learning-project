{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "974d630e-939f-4cbe-afb2-4f8568b42eb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting PyPDF2\n",
      "  Downloading pypdf2-3.0.1-py3-none-any.whl.metadata (6.8 kB)\n",
      "Downloading pypdf2-3.0.1-py3-none-any.whl (232 kB)\n",
      "Installing collected packages: PyPDF2\n",
      "Successfully installed PyPDF2-3.0.1\n"
     ]
    }
   ],
   "source": [
    "!pip install PyPDF2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "236907cb-0899-49cd-b29a-732e079b315f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PDF loaded successfully!\n",
      "\n",
      "User: What is the main topic of the document?\n",
      "Bot : This is a definition/explanation based on the PDF content.\n",
      "\n",
      "User: How is this topic explained? based on previous answer\n",
      "Bot : This is a process explanation from the PDF.\n",
      "\n",
      "User: Why is this important? considering what you said earlier\n",
      "Bot : This is a definition/explanation based on the PDF content.\n",
      "\n",
      "User: Can you give an example? from the same context\n",
      "Bot : Relevant information found in the PDF section.\n",
      "\n",
      "User: What is the conclusion of the document? based on full discussion\n",
      "Bot : This is a definition/explanation based on the PDF content.\n",
      "\n",
      "\n",
      "================ FULL CHAT HISTORY ================\n",
      "\n",
      "Turn 1\n",
      "User: What is the main topic of the document?\n",
      "Bot : This is a definition/explanation based on the PDF content.\n",
      "--------------------------------------------------\n",
      "Turn 2\n",
      "User: How is this topic explained? based on previous answer\n",
      "Bot : This is a process explanation from the PDF.\n",
      "--------------------------------------------------\n",
      "Turn 3\n",
      "User: Why is this important? considering what you said earlier\n",
      "Bot : This is a definition/explanation based on the PDF content.\n",
      "--------------------------------------------------\n",
      "Turn 4\n",
      "User: Can you give an example? from the same context\n",
      "Bot : Relevant information found in the PDF section.\n",
      "--------------------------------------------------\n",
      "Turn 5\n",
      "User: What is the conclusion of the document? based on full discussion\n",
      "Bot : This is a definition/explanation based on the PDF content.\n",
      "--------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "from PyPDF2 import PdfReader\n",
    "\n",
    "class PDFChatbot:\n",
    "    def __init__(self, pdf_path):\n",
    "        self.pdf_path = pdf_path\n",
    "        self.text = \"\"\n",
    "        self.history = []  \n",
    "\n",
    "    def load_pdf(self):\n",
    "        reader = PdfReader(self.pdf_path)\n",
    "        for page in reader.pages:\n",
    "            self.text += page.extract_text() + \"\\n\"\n",
    "        print(\"PDF loaded successfully!\\n\")\n",
    "\n",
    "    def get_answer(self, question):\n",
    "    \n",
    "        question = question.lower()\n",
    "\n",
    "        if \"what\" in question:\n",
    "            return \"This is a definition/explanation based on the PDF content.\"\n",
    "        elif \"how\" in question:\n",
    "            return \"This is a process explanation from the PDF.\"\n",
    "        elif \"why\" in question:\n",
    "            return \"This is a reasoning-based answer from the PDF.\"\n",
    "        else:\n",
    "            return \"Relevant information found in the PDF section.\"\n",
    "\n",
    "    def chat(self, question):\n",
    "        answer = self.get_answer(question)\n",
    "\n",
    "        self.history.append({\"user\": question, \"bot\": answer})\n",
    "\n",
    "        print(f\"User: {question}\")\n",
    "        print(f\"Bot : {answer}\\n\")\n",
    "\n",
    "        return answer\n",
    "    def print_history(self):\n",
    "        print(\"\\n================ FULL CHAT HISTORY ================\\n\")\n",
    "        for i, turn in enumerate(self.history, 1):\n",
    "            print(f\"Turn {i}\")\n",
    "            print(\"User:\", turn[\"user\"])\n",
    "            print(\"Bot :\", turn[\"bot\"])\n",
    "            print(\"--------------------------------------------------\")\n",
    "\n",
    "pdf_path = r\"C:\\Users\\amrit\\Downloads\\survey cdc.pdf\" \n",
    "\n",
    "bot = PDFChatbot(pdf_path)\n",
    "bot.load_pdf()\n",
    "q1 = \"What is the main topic of the document?\"\n",
    "a1 = bot.chat(q1)\n",
    "\n",
    "q2 = \"How is this topic explained?\"\n",
    "a2 = bot.chat(q2 + \" based on previous answer\")\n",
    "\n",
    "q3 = \"Why is this important?\"\n",
    "a3 = bot.chat(q3 + \" considering what you said earlier\")\n",
    "\n",
    "q4 = \"Can you give an example?\"\n",
    "a4 = bot.chat(q4 + \" from the same context\")\n",
    "\n",
    "q5 = \"What is the conclusion of the document?\"\n",
    "a5 = bot.chat(q5 + \" based on full discussion\")\n",
    "bot.print_history()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4644b7d6-3c92-4e9f-a207-5fcdfb90ddc5",
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
