from langchain.prompts import PromptTemplate

simple_prompt = PromptTemplate.from_template(
    """
    Generate gloss in Ukrainian WordNet for lemma {lemma_ukr}
    which is lemma {lemma_eng} in English WordNet, 
    based on gloss from English Wordnet: {gloss}
    and its translation in Ukrainian: {gloss_trans1}, {gloss_trans2} 
    Make the answer grammatically correct, be careful with word conjugation. 
    You don't have to include all information from the source material. 
    Answer with only gloss.
    """
)

guideline_prompt = PromptTemplate.from_template(
    """
    Your task is to propose your variant of Ukrainian gloss for a lemma in Ukrainian WordNet.
    To solve the problem do the following:
        - First, analyze given English gloss, its translations into Ukrainian and dictionanry definition in Ukrainian
        - Then evaluate each of the variants, and based on given information create your own gloss
        - Make the answer grammatically correct, pay special attention to the conjugation
        - Return only ukrainian gloss 

    Use the following format:
    Ukrainian lemma:
    ```
    ukrainian lemma here
    ```

    English lemma:
    ```
    english lemma here
    ```

    Gloss from English WordNet:
    ```
    gloss from english wordnet here
    ```

    Gloss translations:
    ```
    one or multiple translation of english gloss into ukrainian elimited by <>
    ```

    Dictionary definition:
    ```
    dictionary definition of ukrainian lemma here
    ```

    Your answer:
    ```
    Ukrainian gloss that you propose here 
    ```

    Ukrainian lemma:
    ```
    {lemma_ukr}
    ```

    English lemma:
    ```
    {lemma_eng}
    ```

    Gloss from English WordNet:
    ```
    {gloss}
    ```

    Gloss translations:
    ```
    <{gloss_trans1}>
    <{gloss_trans2}>
    ```

    Dictionary definition:
    ```
    <{dict_def1}>
    <{dict_def2}>
    ```

    Answer only with ukrainian gloss that you generated. Do not include lemma.
    
    Check once again wheher your answer doesn't contain any extra words except from a gloss that you generated.
    For example phrase like ```Український глос:``` shouldn't be in a final answer.
    """
)

guideline_prompt_with_reasoning = PromptTemplate.from_template(
    """
    Your task is to propose your variant of Ukrainian gloss for a lemma in Ukrainian WordNet.
    To solve the problem do the following:
        - First, analyze given English gloss, and its translations into Ukrainian
        - Then evaluate each of the variants, and based on given information create your own gloss
        - Make the answer grammatically correct, pay special attention to the conjugation
    
    Give output in following format:
    ```
    gloss: gloss that you generated
    reasoning: explain why you choose this gloss
    ```

    Use the following format:
    Ukrainian lemma:
    ```
    ukrainian lemma here
    ```

    English lemma:
    ```
    english lemma here
    ```

    Gloss from English WordNet:
    ```
    gloss from english wordnet here
    ```

    Gloss translations:
    ```
    one or multiple translation of english gloss into ukrainian elimited by <>
    ```

    Dictionary definition:
    ```
    dictionary definition of ukrainian lemma here
    ```

    Your answer:
    ```
    Ukrainian gloss that you propose here 
    ```

    Ukrainian lemma:
    ```
    {lemma_ukr}
    ```

    English lemma:
    ```
    {lemma_eng}
    ```

    Gloss from English WordNet:
    ```
    {gloss}
    ```

    Gloss translations:
    ```
    <{gloss_trans1}>
    <{gloss_trans2}>
    ```

    Check if the output is in following format:
    ```gloss```: only gloss that you generated
    ```reasoning```: add here any additional information that you think is important
    """
)