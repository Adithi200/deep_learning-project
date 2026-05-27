{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5af9d4e6-411e-44fa-9d45-6f4e03004e3e",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'sentence_transformers'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msentence_transformers\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m SentenceTransformer\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msklearn\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mmetrics\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mpairwise\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m cosine_similarity\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'sentence_transformers'"
     ]
    }
   ],
   "source": [
    "from sentence_transformers import SentenceTransformer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "import pandas as pd\n",
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
    "model = SentenceTransformer('all-MiniLM-L6-v2')\n",
    "embeddings = model.encode(sentences)\n",
    "similarity_matrix = cosine_similarity(embeddings)\n",
    "df = pd.DataFrame(\n",
    "    similarity_matrix,\n",
    "    index=[f\"S{i+1}\" for i in range(len(sentences))],\n",
    "    columns=[f\"S{i+1}\" for i in range(len(sentences))]\n",
    ")\n",
    "print(\"\\nSentences:\\n\")\n",
    "\n",
    "for i, sentence in enumerate(sentences):\n",
    "    print(f\"S{i+1}: {sentence}\")\n",
    "print(\"\\nCosine Similarity Matrix:\\n\")\n",
    "print(df.round(2))\n",
    "print(\"\\nVerification:\")\n",
    "print(\"Cricket sentences show higher similarity with other cricket sentences.\")\n",
    "print(\"Cooking sentences are more similar to cooking-related sentences.\")\n",
    "print(\"Programming sentences are closer to programming-related sentences.\")\n",
    "print(\"Cross-topic similarities are generally lower.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "521c1c93-94b6-4dd7-aa27-7c0f205522d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: sentence-transformers in c:\\users\\amrit\\anaconda3\\lib\\site-packages (5.5.1)\n",
      "Requirement already satisfied: transformers<6.0.0,>=4.41.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (5.9.0)\n",
      "Requirement already satisfied: huggingface-hub>=0.23.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.16.4)\n",
      "Requirement already satisfied: torch>=1.11.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (2.12.0)\n",
      "Requirement already satisfied: numpy>=1.20.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (2.3.5)\n",
      "Requirement already satisfied: scikit-learn>=0.22.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.7.2)\n",
      "Requirement already satisfied: scipy>=1.0.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.16.3)\n",
      "Requirement already satisfied: typing_extensions>=4.5.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (4.15.0)\n",
      "Requirement already satisfied: tqdm>=4.0.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sentence-transformers) (4.67.1)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (25.0)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (6.0.3)\n",
      "Requirement already satisfied: regex>=2025.10.22 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (2026.5.9)\n",
      "Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (0.22.2)\n",
      "Requirement already satisfied: typer in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (0.20.0)\n",
      "Requirement already satisfied: safetensors>=0.4.3 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (0.7.0)\n",
      "Requirement already satisfied: click>=8.4.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (8.4.1)\n",
      "Requirement already satisfied: filelock>=3.10.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (3.20.0)\n",
      "Requirement already satisfied: fsspec>=2023.5.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (2025.10.0)\n",
      "Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (1.5.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (0.28.1)\n",
      "Requirement already satisfied: anyio in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->sentence-transformers) (4.10.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->sentence-transformers) (2026.4.22)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->sentence-transformers) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub>=0.23.0->sentence-transformers) (3.11)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub>=0.23.0->sentence-transformers) (0.16.0)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (1.5.4)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (14.2.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from click>=8.4.0->huggingface-hub>=0.23.0->sentence-transformers) (0.4.6)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from rich>=10.11.0->typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from rich>=10.11.0->typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (2.19.2)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (0.1.2)\n",
      "Requirement already satisfied: joblib>=1.2.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from scikit-learn>=0.22.0->sentence-transformers) (1.5.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from scikit-learn>=0.22.0->sentence-transformers) (3.5.0)\n",
      "Requirement already satisfied: setuptools<82 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (80.9.0)\n",
      "Requirement already satisfied: sympy>=1.13.3 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (1.14.0)\n",
      "Requirement already satisfied: networkx>=2.5.1 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (3.5)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (3.1.6)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from sympy>=1.13.3->torch>=1.11.0->sentence-transformers) (1.3.0)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from anyio->httpx<1,>=0.23.0->huggingface-hub>=0.23.0->sentence-transformers) (1.3.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\amrit\\anaconda3\\lib\\site-packages (from jinja2->torch>=1.11.0->sentence-transformers) (3.0.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install sentence-transformers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cce8c6e5-9a7c-4810-833a-e63b99506b42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dc5fc2c65fc641eb83afac5ab93b84e0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "modules.json:   0%|          | 0.00/349 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "38c5ffa805a74f828d7014c5065d17ed",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "config_sentence_transformers.json:   0%|          | 0.00/116 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a6728ab3bc75414a95d1610abf056b88",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "README.md:   0%|          | 0.00/10.5k [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "eeb0adab070b4e83a597a807f7ee5270",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "sentence_bert_config.json:   0%|          | 0.00/53.0 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "158bd61321d048bbbee53b1e3a8f3915",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "config.json:   0%|          | 0.00/612 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ba7d47f747fb4874b7c558df04e4ca32",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "model.safetensors:   0%|          | 0.00/90.9M [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dc2e7b2e696248d29aa6b259aa8f5653",
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
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6f3d0699f39c4c1db601d441f22fab56",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "tokenizer_config.json:   0%|          | 0.00/350 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1df23a189dbf4952b57c948e9df39661",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "vocab.txt:   0%|          | 0.00/232k [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7d831c6f66234fa2a38647e73b98b281",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "tokenizer.json:   0%|          | 0.00/466k [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d3d455751bb449669448f4f6aedf1211",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "special_tokens_map.json:   0%|          | 0.00/112 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "de2e59b484e041aabc37240465d41149",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "config.json:   0%|          | 0.00/190 [00:00<?, ?B/s]"
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
      "Sentences:\n",
      "\n",
      "S1: Virat Kohli scored a century in the cricket match.\n",
      "S2: The bowler took five wickets in the tournament.\n",
      "S3: India won the T20 series by six runs.\n",
      "S4: The batsman hit a powerful cover drive.\n",
      "S5: Pasta tastes better with fresh tomato sauce.\n",
      "S6: The chef prepared spicy chicken curry.\n",
      "S7: Baking a cake requires flour and eggs.\n",
      "S8: Python is widely used for machine learning.\n",
      "S9: Functions help organize code efficiently.\n",
      "S10: Debugging is an important programming skill.\n",
      "\n",
      "Cosine Similarity Matrix:\n",
      "\n",
      "       S1    S2    S3    S4    S5    S6    S7    S8    S9   S10\n",
      "S1   1.00  0.51  0.51  0.45  0.03  0.20  0.02 -0.00 -0.02 -0.01\n",
      "S2   0.51  1.00  0.60  0.50  0.04  0.24  0.08  0.05  0.04  0.04\n",
      "S3   0.51  0.60  1.00  0.39  0.01  0.14  0.04 -0.01 -0.00 -0.07\n",
      "S4   0.45  0.50  0.39  1.00 -0.05  0.18 -0.05 -0.00 -0.03  0.01\n",
      "S5   0.03  0.04  0.01 -0.05  1.00  0.25  0.07  0.13  0.05  0.03\n",
      "S6   0.20  0.24  0.14  0.18  0.25  1.00  0.09  0.04  0.05 -0.05\n",
      "S7   0.02  0.08  0.04 -0.05  0.07  0.09  1.00 -0.09  0.11  0.02\n",
      "S8  -0.00  0.05 -0.01 -0.00  0.13  0.04 -0.09  1.00  0.29  0.31\n",
      "S9  -0.02  0.04 -0.00 -0.03  0.05  0.05  0.11  0.29  1.00  0.48\n",
      "S10 -0.01  0.04 -0.07  0.01  0.03 -0.05  0.02  0.31  0.48  1.00\n",
      "\n",
      "Verification:\n",
      "Cricket sentences show higher similarity with other cricket sentences.\n",
      "Cooking sentences are more similar to cooking-related sentences.\n",
      "Programming sentences are closer to programming-related sentences.\n",
      "Cross-topic similarities are generally lower.\n"
     ]
    }
   ],
   "source": [
    "from sentence_transformers import SentenceTransformer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "import pandas as pd\n",
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
    "model = SentenceTransformer('all-MiniLM-L6-v2')\n",
    "embeddings = model.encode(sentences)\n",
    "similarity_matrix = cosine_similarity(embeddings)\n",
    "df = pd.DataFrame(\n",
    "    similarity_matrix,\n",
    "    index=[f\"S{i+1}\" for i in range(len(sentences))],\n",
    "    columns=[f\"S{i+1}\" for i in range(len(sentences))]\n",
    ")\n",
    "print(\"\\nSentences:\\n\")\n",
    "\n",
    "for i, sentence in enumerate(sentences):\n",
    "    print(f\"S{i+1}: {sentence}\")\n",
    "print(\"\\nCosine Similarity Matrix:\\n\")\n",
    "print(df.round(2))\n",
    "print(\"\\nVerification:\")\n",
    "print(\"Cricket sentences show higher similarity with other cricket sentences.\")\n",
    "print(\"Cooking sentences are more similar to cooking-related sentences.\")\n",
    "print(\"Programming sentences are closer to programming-related sentences.\")\n",
    "print(\"Cross-topic similarities are generally lower.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24cd8244-7b59-4935-97bb-2368595c4fbd",
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
