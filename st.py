

import streamlit as st



def create_blog():
    category = st.selectbox("Category", ["Marketing", "Sales", "Advertisment"])
    type_1 = st.selectbox("Type", ["General", "Goal Specific"])
    word_count= st.number_input("Word Count")
    title = st.text_input("Title")
    outline = st.text_area("Outline")
    topic = st.text_input("TOPIC (COMPULSORY)", key='topic')
    audience = st.text_input("Audience")
    supporting_data = st.text_area("Supporting data/stats/tips/science/evidence")
    reference = st.text_area("reference/inspiration/example")
    word_complexity = st.text_input("word complexity")
    purpose = st.text_input("Purpose")
    seo = st.text_input("SEO")
    hyperlinks = st.text_input("hyperlinks")
    other_details = st.text_area("other specific details")
    if st.button("Create Blog"):
        prompt = f"Do what is mentioned here :  {topic} based on the: {word_count},{title},{outline},{audience},{supporting_data},{reference},{word_complexity},{purpose},{seo},{hyperlinks},{other_details}"
        completion = openai.Completion.create(model="text-davinci-003",
                                                prompt=prompt,
                                                temperature = 0.5,max_tokens=1024,
                                                top_p=1,frequency_penalty=0.0,
                                                presence_penalty=0)
        blog_content = completion.choices[0].text
        result = f"## {title}\n\n{blog_content}"
        st.write(result)

st.title("Blog Writing App")
st.write("Enter your blog information below:")
create_blog()







