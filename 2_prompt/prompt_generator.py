from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = """ Summarize the paper named as {paper_input}, 
        length of the summzary should be {lengh_input}
        """ ,
    input_variables = ["paper_input", "lengh_input"],
    validate_template = True   
)

template.save("template.json")