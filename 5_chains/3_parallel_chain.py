# Text -> prompt -> Notes and Quiz -> Show to user

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.runnables import RunnableParallel

# API
load_dotenv()

# Model: 
chat_model1 = ChatGroq(
    model = "llama-3.1-8b-instant"
)


# Create endpoint: 
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

# wrapper
chat_model2 = ChatHuggingFace(
    llm =llm
)


# Prompt : 
prompt1 = PromptTemplate(
    template = "Generate short and simple notes of following text: \n {text}", 
    input_variables = ["text"]
)

prompt2 = PromptTemplate(
    template = "Generate the 5 short question answers from the following text: \n {text}",
    input_variables= ["text"]
)

prompt3 =PromptTemplate(
    template ="Merge the provided notes and quiz into a single document: \n notes -> {notes} \n quiz -> {quiz}",
    input_variables = ["notes", "quiz"]
)


# Parser: 
parser = StrOutputParser()

# Chain: 
# Paraller Chain

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | chat_model1 | parser, 
        'quiz' : prompt2 | chat_model2 | parser
    }
)

# Merger Chain
merge_chain = prompt3 | chat_model1 | parser


# Combined chain: 
chain = parallel_chain | merge_chain | parser

text = "A support vector machine (SVM) is a supervised machine learning algorithm that classifies data by finding an optimal line or hyperplane that maximizes the distance between each class in an N-dimensional space. SVMs were developed in the 1990s by Vladimir N. Vapnik and his colleagues, and they published this work in a paper titled Support Vector Method for Function Approximation, Regression Estimation, and Signal Processing 1 in 1995. SVMs are commonly used within classification problems. They distinguish between two classes by finding the optimal hyperplane that maximizes the margin between the closest data points of opposite classes. The number of features in the input data determine if the hyperplane is a line in a 2-D space or a plane in a n-dimensional space. Since multiple hyperplanes can be found to differentiate classes, maximizing the margin between points enables the algorithm to find the best decision boundary between classes. This, in turn, enables it to generalize well to new data and make accurate classification predictions. The lines that are adjacent to the optimal hyperplane are known as support vectors as these vectors run through the data points that determine the maximal margin. The SVM algorithm is widely used in machine learning as it can handle both linear and nonlinear classification tasks. However, when the data is not linearly separable, kernel functions are used to transform the data higher-dimensional space to enable linear separation. This application of kernel functions can be known as the “kernel trick”, and the choice of kernel function, such as linear kernels, polynomial kernels, radial basis function (RBF) kernels, or sigmoid kernels, depends on data characteristics and the specific use case."

response = chain.invoke({'text': text})

print(response)

chain.get_graph().print_ascii()