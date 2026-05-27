{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e4b5fdf-691f-4900-bba1-5ff10bf7b29c",
   "metadata": {},
   "outputs": [],
   "source": [
    "facts_db = {\n",
    "    \"population of india\": \"1.44 billion\",\n",
    "    \"speed of light\": \"3x10^8 m/s\",\n",
    "    \"days in a year\": \"365\",\n",
    "    \"hours in a day\": \"24\"\n",
    "}\n",
    "def lookup(fact):\n",
    "\n",
    "    fact = fact.lower()\n",
    "\n",
    "    return facts_db.get(fact, \"Fact not found\")\n",
    "\n",
    "def calculate(expression):\n",
    "\n",
    "    try:\n",
    "        return eval(expression)\n",
    "\n",
    "    except Exception as e:\n",
    "        return f\"Calculation Error: {e}\"\n",
    "\n",
    "def react_agent(question):\n",
    "\n",
    "    print(\"\\nUSER QUESTION:\")\n",
    "    print(question)\n",
    "\n",
    "    print(\"\\nTHOUGHT:\")\n",
    "    print(\"I need to lookup the population of India first.\")\n",
    "    print(\"\\nACTION: lookup('population of india')\")\n",
    "\n",
    "    population = lookup(\"population of india\")\n",
    "\n",
    "    print(\"OBSERVATION:\", population)\n",
    "    population_number = 1.44 * 1000000000\n",
    "\n",
    "    print(\"\\nTHOUGHT:\")\n",
    "    print(\"Now I need to calculate 10% of the population.\")\n",
    "\n",
    "    expression = f\"{population_number} * 0.10\"\n",
    "\n",
    "    print(f\"\\nACTION: calculate('{expression}')\")\n",
    "\n",
    "    result = calculate(expression)\n",
    "\n",
    "    print(\"OBSERVATION:\", result)\n",
    "\n",
    "    print(\"\\nFINAL ANSWER:\")\n",
    "    print(f\"10% of India's population is approximately {result:.0f} people.\")\n",
    "\n",
    "question = \"\"\"\n",
    "What is 10% of the population of India?\n",
    "\"\"\"\n",
    "\n",
    "react_agent(question)"
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
