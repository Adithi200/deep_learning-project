{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "eac8d32b-ce98-4cb8-addd-a6407ccd47f3",
   "metadata": {
    "scrolled": true
   },
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
    "\n",
    "    print(\"\\n==============================\")\n",
    "    print(\"Query:\", query)\n",
    "\n",
    "    results = retriever.invoke(query)\n",
    "\n",
    "    for i, doc in enumerate(results):\n",
    "\n",
    "        print(f\"\\nTop {i+1} Result:\")\n",
    "        print(doc.page_content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "395ecd5c-14fc-4cf6-920a-47274c216c96",
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
