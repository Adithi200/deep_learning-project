{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "90b3cf66-389f-461e-99ac-d590f0a5f946",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\amrit\\AppData\\Local\\Temp\\ipykernel_16400\\3010329410.py:1: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.\n",
      "  from langchain_community.vectorstores import FAISS\n",
      "C:\\Users\\amrit\\AppData\\Local\\Temp\\ipykernel_16400\\3010329410.py:15: LangChainDeprecationWarning: The class `HuggingFaceEmbeddings` was deprecated in LangChain 0.2.2 and will be removed in 1.0. An updated version of the class exists in the `langchain-huggingface package and should be used instead. To use it run `pip install -U `langchain-huggingface` and import as `from `langchain_huggingface import HuggingFaceEmbeddings``.\n",
      "  embeddings = HuggingFaceEmbeddings(model_name=\"all-MiniLM-L6-v2\")\n",
      "Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a3df8390a9224d44b0fe01644b12fd33",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "==============================\n",
      "Query: A cricket player scored runs\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'VectorStoreRetriever' object has no attribute 'get_relevant_documents'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 26\u001b[39m\n\u001b[32m     24\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[33m==============================\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m     25\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mQuery:\u001b[39m\u001b[33m\"\u001b[39m, query)\n\u001b[32m---> \u001b[39m\u001b[32m26\u001b[39m results = \u001b[43mretriever\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget_relevant_documents\u001b[49m(query)\n\u001b[32m     27\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m i, doc \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(results):\n\u001b[32m     28\u001b[39m     \u001b[38;5;28mprint\u001b[39m(\u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[33mTop \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mi+\u001b[32m1\u001b[39m\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m Result:\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\anaconda3\\Lib\\site-packages\\pydantic\\main.py:1026\u001b[39m, in \u001b[36mBaseModel.__getattr__\u001b[39m\u001b[34m(self, item)\u001b[39m\n\u001b[32m   1023\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28msuper\u001b[39m().\u001b[34m__getattribute__\u001b[39m(item)  \u001b[38;5;66;03m# Raises AttributeError if appropriate\u001b[39;00m\n\u001b[32m   1024\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m   1025\u001b[39m     \u001b[38;5;66;03m# this is the current error\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m1026\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mAttributeError\u001b[39;00m(\u001b[33mf\u001b[39m\u001b[33m'\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mtype\u001b[39m(\u001b[38;5;28mself\u001b[39m).\u001b[34m__name__\u001b[39m\u001b[38;5;132;01m!r}\u001b[39;00m\u001b[33m object has no attribute \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mitem\u001b[38;5;132;01m!r}\u001b[39;00m\u001b[33m'\u001b[39m)\n",
      "\u001b[31mAttributeError\u001b[39m: 'VectorStoreRetriever' object has no attribute 'get_relevant_documents'"
     ]
    }
   ],
   "source": [
    "from langchain_community.vectorstores import FAISS\n",
    "from langchain_community.embeddings import HuggingFaceEmbeddings\n",
    "sentences = [\n",
    "    \"Virat Kohli scored a century in the cricket match.\",\n",
    "    \"The bowler took five wickets in the tournament.\",\n",
    "    \"India won the T20 series by six runs.\",\n",
    "    \"The batsman hit a powerful cover drive.\",\n",
    "    \"Pasta tastes better with fresh tomato sauce.\",\n",
    "    \"The chef prepared spicy chicken curry.\",\n",
    "    \"Baking a cake requires flour and eggs.\",\n",
    "    \"Python is widely used for machine learning.\",\n",
    "    \"Functions help organize code efficiently.\",\n",
    "    \"Debugging is an important programming skill.\"\n",
    "]\n",
    "embeddings = HuggingFaceEmbeddings(model_name=\"all-MiniLM-L6-v2\")\n",
    "vectorstore = FAISS.from_texts(sentences, embedding=embeddings)\n",
    "retriever = vectorstore.as_retriever(search_kwargs={\"k\": 3})\n",
    "queries = [\n",
    "    \"A cricket player scored runs\",\n",
    "    \"How to bake a cake\",\n",
    "    \"Python coding and debugging\"\n",
    "]\n",
    "for query in queries:\n",
    "    print(\"\\n==============================\")\n",
    "    print(\"Query:\", query)\n",
    "    results = retriever.get_relevant_documents(query)\n",
    "    for i, doc in enumerate(results):\n",
    "        print(f\"\\nTop {i+1} Result:\")\n",
    "        print(\"Sentence:\", doc.page_content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b5b98818-8863-4066-bbf1-e635c7465bff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "==============================\n",
      "Query: A cricket player scored runs\n",
      "\n",
      "Top 1 Result:\n",
      "Virat Kohli scored a century in the cricket match.\n",
      "\n",
      "Top 2 Result:\n",
      "The batsman hit a powerful cover drive.\n",
      "\n",
      "Top 3 Result:\n",
      "The bowler took five wickets in the tournament.\n",
      "\n",
      "==============================\n",
      "Query: How to bake a cake\n",
      "\n",
      "Top 1 Result:\n",
      "Baking a cake requires flour and eggs.\n",
      "\n",
      "Top 2 Result:\n",
      "The chef prepared spicy chicken curry.\n",
      "\n",
      "Top 3 Result:\n",
      "The bowler took five wickets in the tournament.\n",
      "\n",
      "==============================\n",
      "Query: Python coding and debugging\n",
      "\n",
      "Top 1 Result:\n",
      "Debugging is an important programming skill.\n",
      "\n",
      "Top 2 Result:\n",
      "Python is widely used for machine learning.\n",
      "\n",
      "Top 3 Result:\n",
      "Functions help organize code efficiently.\n"
     ]
    }
   ],
   "source": [
    "for query in queries:\n",
    "    print(\"\\n==============================\")\n",
    "    print(\"Query:\", query)\n",
    "\n",
    "    results = retriever.invoke(query)\n",
    "\n",
    "    for i, doc in enumerate(results):\n",
    "        print(f\"\\nTop {i+1} Result:\")\n",
    "        print(doc.page_content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc6b9e89-8dd1-4b91-84c2-3601574cc935",
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
