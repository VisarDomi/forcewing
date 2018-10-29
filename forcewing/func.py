from forcewing.models import Portfolio, Blog

#admin
def save_picture(form_picture, dest_folder, output_size_1, output_size_2):
    """
    save_picture saves picture from user input to static folder, hashing the filename  
    form_picture is the file name of the input
    dest_folder is the folder where the image will be saved
    """
    random_hex = secrets.token_hex(8) #8 bytes
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(os.path.dirname(bp.root_path), 'static/', dest_folder, picture_fn)
    output_size = (output_size_1, output_size_2)
    i = Image.open(form_picture)
    i = i.convert('RGB')
    i = ImageOps.fit(i, output_size, Image.ANTIALIAS)
    i.save(picture_path)
    return picture_fn

#main
def send_contact_email(name, email, message):
    #send a email to recipients from sender with the following arguments as information

    msg = Message('Forcewing', sender='forcewing.worker@gmail.com', recipients=['ronalddomi4@gmail.com'])
    msg.body = f'''Someone just submitted your form on forcewing.com, here's what they had to say:
    ------
    Name:  {name}

    Email:  {email}

    Message:  {message}
    
    '''
    mail.send(msg)

# portfolio
def change_text_content(id):
    portfolio = Portfolio.query.filter_by(id=id).first()
    lines = portfolio.content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string = str(text)
            html.append(string)
    return html

# blog
def change_text_section_content(id):
    blog = Blog.query.filter_by(id=id).first()
    lines = blog.section_content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string = str(text)
            html.append(string)
    return html

#blog
def change_text_subsection_content(id):
    blog = Blog.query.filter_by(id=id).first()
    lines = blog.subsection_content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string = str(text)
            html.append(string)
    return html
