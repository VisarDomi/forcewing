from app import db
from app.models import User, Blog, Category, Tag, Portfolio
# from flask_login import login_user
from flask import url_for

db.drop_all()
db.create_all()

user = User(username='Forcewing')
user.set_password('forcewing')
db.session.add(user)
# login_user(user)
# category1 = Category(name='Smartphone')
# db.session.add(category1)
# category2 = Category(name='blogtest')
# db.session.add(category2)
# category3 = Category(name='iphones')
# db.session.add(category3)

# blog1 = Blog(title='Iphone 5s', 
#             subtitle='Iphones are cool',
#             section_title='Lorum ipsum',
#             section_content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius. Vitae nunc sed velit dignissim sodales. Aliquet risus feugiat in ante. Eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus. Orci a scelerisque purus semper eget duis. Pellentesque habitant morbi tristique senectus et netus et. Pharetra convallis posuere morbi leo urna molestie at. Hendrerit dolor magna eget est lorem ipsum dolor sit. Eget nulla facilisi etiam dignissim. Bibendum at varius vel pharetra vel.\r\n\r\nVenenatis tellus in metus vulputate eu scelerisque felis imperdiet. Ipsum consequat nisl vel pretium lectus quam id leo in. Fermentum leo vel orci porta non pulvinar neque laoreet suspendisse. Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. At ultrices mi tempus imperdiet nulla malesuada. In hendrerit gravida rutrum quisque non tellus orci ac. Ultricies lacus sed turpis tincidunt id aliquet. Morbi enim nunc faucibus a pellentesque sit amet. Orci ac auctor augue mauris augue neque gravida in fermentum. Vitae ultricies leo integer malesuada. Dignissim suspendisse in est ante in nibh mauris cursus mattis. Amet mauris commodo quis imperdiet massa tincidunt nunc pulvinar. Volutpat sed cras ornare arcu. Tortor at auctor urna nunc id cursus.\r\n\r\nSit amet dictum sit amet justo donec enim diam. Aliquet sagittis id consectetur purus ut faucibus pulvinar elementum. Scelerisque varius morbi enim nunc faucibus a pellentesque. Pretium vulputate sapien nec sagittis aliquam. Vel pretium lectus quam id. Faucibus vitae aliquet nec ullamcorper sit amet risus nullam. Interdum consectetur libero id faucibus nisl tincidunt eget nullam non. Maecenas ultricies mi eget mauris pharetra et ultrices. Augue eget arcu dictum varius duis. Euismod lacinia at quis risus sed vulputate odio. Tristique et egestas quis ipsum suspendisse ultrices gravida. Sem integer vitae justo eget magna fermentum.\r\n\r\nDiam volutpat commodo sed egestas egestas fringilla phasellus. Quam viverra orci sagittis eu. Enim nec dui nunc mattis enim ut tellus elementum sagittis. Imperdiet sed euismod nisi porta. Elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue. Id diam maecenas ultricies mi eget mauris pharetra et ultrices. Sit amet consectetur adipiscing elit ut aliquam purus. Sed risus ultricies tristique nulla aliquet enim tortor. Vehicula ipsum a arcu cursus. Faucibus vitae aliquet nec ullamcorper sit amet risus. Ultricies lacus sed turpis tincidunt. Et malesuada fames ac turpis egestas. Donec adipiscing tristique risus nec feugiat. Convallis posuere morbi leo urna molestie at elementum. Vitae et leo duis ut diam quam. Lorem donec massa sapien faucibus et. Duis tristique sollicitudin nibh sit amet commodo nulla facilisi.\r\n\r\nScelerisque varius morbi enim nunc faucibus a pellentesque sit. Non odio euismod lacinia at quis risus sed vulputate. Aliquet risus feugiat in ante metus. In arcu cursus euismod quis viverra nibh. Arcu non odio euismod lacinia at quis. In hac habitasse platea dictumst quisque sagittis. Tristique senectus et netus et malesuada fames ac. Bibendum neque egestas congue quisque egestas. Scelerisque purus semper eget duis at tellus at urna condimentum. Et netus et malesuada fames ac. Enim blandit volutpat maecenas volutpat. Egestas pretium aenean pharetra magna ac placerat vestibulum. Cum sociis natoque penatibus et magnis. Nec dui nunc mattis enim. Ullamcorper sit amet risus nullam eget. Odio tempor orci dapibus ultrices in iaculis nunc sed augue. Lectus arcu bibendum at varius vel pharetra vel. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla. Nunc mattis enim ut tellus elementum. Non blandit massa enim nec dui nunc.\r\n\r\nJusto laoreet sit amet cursus sit amet dictum sit amet. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec. Proin sagittis nisl rhoncus mattis rhoncus. Erat imperdiet sed euismod nisi porta lorem mollis. Augue neque gravida in fermentum et sollicitudin. Arcu risus quis varius quam quisque. Enim blandit volutpat maecenas volutpat blandit. Urna molestie at elementum eu facilisis sed. Risus nec feugiat in fermentum posuere urna nec. Commodo odio aenean sed adipiscing diam donec adipiscing tristique. Sit amet cursus sit amet. Volutpat sed cras ornare arcu. Sed libero enim sed faucibus turpis. Quis ipsum suspendisse ultrices gravida dictum fusce ut. Porttitor eget dolor morbi non arcu risus quis varius quam. Nibh sit amet commodo nulla facilisi nullam.',
#             subsection_title='Lorum ipsum 2',
#             subsection_content='Consectetur purus ut faucibus pulvinar elementum integer enim neque. Integer feugiat scelerisque varius morbi enim. Dui nunc mattis enim ut tellus elementum. Nunc lobortis mattis aliquam faucibus purus in. Sed libero enim sed faucibus turpis in. Vel quam elementum pulvinar etiam. Tristique senectus et netus et malesuada fames. Ut placerat orci nulla pellentesque dignissim enim sit amet venenatis. Tortor condimentum lacinia quis vel eros donec. Tortor condimentum lacinia quis vel. Fermentum dui faucibus in ornare quam viverra orci sagittis eu. Id velit ut tortor pretium viverra suspendisse potenti nullam. Tristique senectus et netus et malesuada fames ac turpis egestas. Amet massa vitae tortor condimentum lacinia quis vel. Id leo in vitae turpis massa. Vulputate dignissim suspendisse in est ante.\r\n\r\nId consectetur purus ut faucibus pulvinar elementum integer enim. Sit amet mattis vulputate enim nulla aliquet porttitor lacus. Tristique risus nec feugiat in fermentum. Massa eget egestas purus viverra accumsan in. Elementum sagittis vitae et leo duis ut diam quam nulla. Mi proin sed libero enim. Ridiculus mus mauris vitae ultricies leo integer malesuada. Auctor augue mauris augue neque gravida in fermentum. Risus feugiat in ante metus dictum at. Felis eget nunc lobortis mattis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec. Varius duis at consectetur lorem donec. Faucibus nisl tincidunt eget nullam non. Pellentesque sit amet porttitor eget dolor morbi non. Nunc sed id semper risus in hendrerit. Nisi scelerisque eu ultrices vitae auctor eu augue.\r\n\r\nQuisque non tellus orci ac auctor augue mauris. Interdum velit laoreet id donec ultrices tincidunt arcu non sodales. Eget gravida cum sociis natoque penatibus et magnis. Nullam ac tortor vitae purus faucibus ornare suspendisse sed nisi. Morbi enim nunc faucibus a pellentesque sit. Turpis egestas integer eget aliquet nibh praesent tristique magna sit. Sed blandit libero volutpat sed cras. Nulla pharetra diam sit amet nisl suscipit adipiscing bibendum est. Nec feugiat nisl pretium fusce id velit ut. Dui vivamus arcu felis bibendum ut tristique. Porttitor rhoncus dolor purus non enim praesent. Cursus sit amet dictum sit amet justo.\r\n\r\nEget sit amet tellus cras adipiscing. Ut placerat orci nulla pellentesque dignissim enim. Adipiscing diam donec adipiscing tristique. Aliquam vestibulum morbi blandit cursus risus at. Odio euismod lacinia at quis. Sit amet commodo nulla facilisi nullam. Vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt. Sapien eget mi proin sed libero enim. Risus commodo viverra maecenas accumsan. Condimentum mattis pellentesque id nibh tortor id aliquet lectus. Suspendisse sed nisi lacus sed viverra. Sit amet porttitor eget dolor morbi non. Lectus urna duis convallis convallis tellus. Massa massa ultricies mi quis hendrerit. Netus et malesuada fames ac turpis egestas. Ullamcorper eget nulla facilisi etiam dignissim. Sem nulla pharetra diam sit amet nisl suscipit. Lorem dolor sed viverra ipsum nunc. Vulputate sapien nec sagittis aliquam malesuada.',
#             quote='Lorum ipsum or iphones?',
#             category=category1.name,
#             image_file='static/blog_pics/Iphone 5s/9d0897dbbbc347d1.png'.replace(' ', '%20'),
#             author=user)
# db.session.add(blog1)
# blog2 = Blog(title='Test blog', 
#             subtitle='Test blogs are cool',
#             section_title='Paragraphs',
#             section_content='Para1.\r\n\r\nPara2.\r\n\r\nPara3.\r\n\r\nPara4.\r\n\r\nPara5.\r\n\r\nPara6.',
#             subsection_title='Same here',
#             subsection_content='Same1.\r\n\r\nSame2.\r\n\r\nSame3.\r\n\r\nSame4.\r\n\r\nSame5.',
#             quote='Para or same?',
#             category=category2.name,
#             author=user)
# db.session.add(blog2)

tag1 = Tag(name='App')
db.session.add(tag1)
tag2 = Tag(name='Website')
db.session.add(tag2)
tag3 = Tag(name='Web app')
db.session.add(tag3)

portfolio1 = Portfolio(title='Eco Riciklim', 
            subtitle='A focus on sustainability',
            content='This hospital waste recycling company founded 2 years ago had a quick growth due to their professional staff and high tech equipment. To accommodate a better web presence, they contacted us to discuss about building a web site where prospective clients could learn more about them and their work.\r\n\r\nAfter discussing their priorities and the way the company operates, we decided the building blocks of the website and their content. After having the layout in place, we chose colors that matched the company, in order to preserve a unified look.\r\n\r\nThe website is responsive across devices. The design was handcrafted using HTML/CSS, based on the web design standards of the year.',
            tag=tag2.name,
            client_name='Eco Riciklim sh.p.k.',
            website='http://www.ecoriciklim.al/',
            user=user)
db.session.add(portfolio1)

portfolio2 = Portfolio(title='Getaway Albania', 
            subtitle='The uncommon element',
            content='Getaway Albania is a fast moving travel agency offering great deals for trips in Albania and abroad. This company wanted to move from a WordPress solution to something more tailored and personalized to their experience, and we offered just that.\r\n\r\nFeaturing the agency prominent colors, the website gives an intensive experience with carefully chosen images, great design principles and a sleek looking font. More then half of the website was coded from scratch, and the rest was adapted from a best selling travel theme.\r\n\r\nThe website features and admin area, where the trip planners regularly update their trips, images and content. The administrator panel is fully personalized to the needs of the website, having just the right amount of features and control, making it very user friendly.',
            tag=tag2.name,
            client_name='Getaway Albania',
            website='https://getawayalbania.com/',
            user=user)
db.session.add(portfolio2)

portfolio3 = Portfolio(title='Impresa Privacy', 
            subtitle='Information security and privacy',
            content='This italian enterprise has seen a skyrocket growth in the last year, handling clients over all northen italy. Part of the efforts to consolidate credibility were to created a great looking and functional website to showcase the features, services and work of the agency.\r\n\r\nThe colors are consistent and unified across the website, making it look elegant and professional. The latest design standards are applied and executed. The administrator area also is a very elegant, functional and useful where the company can manage their blog, and in future releases, also clients and invoices.',
            tag=tag2.name,
            client_name='Impresa Privacy',
            user=user)
db.session.add(portfolio3)

portfolio4 = Portfolio(title='Lisphera Coaching', 
            subtitle='A whole other world',
            content='This platform is the amazing result of experience, optimized work processes and consolidated design. This coaching platform allows our client to closely follow, analyse and guide their athletes through a centralized system. Once the athletes sign up, they can synchronize their smart watches so their training data is shown on their dashboard.\r\n\r\nThe platform also features social networking features, where athletes can follow and interact with the achievements, records and results of their peers. The administrator area of the coach gives full visibility and control over the athletes, in order to gauge and direct their efforts through training schedules.\r\n\r\nThe images are taken from the Beta 1 version of the site, and functionality will grow with time. Planned features include messaging, reacting to post, implementation of records, achievements and athlete poduims, PDF creating of personal training data etc.',
            tag=tag3.name,
            client_name='Lisphera Coaching',
            user=user)
db.session.add(portfolio4)

portfolio5 = Portfolio(title='The Institution', 
            subtitle='A musical experience',
            content='The creation of this website went through a multitude of variations, making this website one of the most challenging when it comes to front-end work.\r\n\r\nWith a 100% unique design, this work is geared more towards a simplified teaser to the musicians youtube channel.',
            tag=tag2.name,
            client_name='The Institution',
            website='http://www.institutionthe.com/',
            user=user)
db.session.add(portfolio5)

portfolio6 = Portfolio(title='Univercity', 
            subtitle='Student hostel',
            content="Univercity is a student hostel situated in Bolzano, Italy. The website is a way to offer incoming students a glimpse into the hostel's various aspects.\r\n\r\nA clean and spacious design allows the unfolding of the hostel section after section.",
            tag=tag2.name,
            client_name='Univercity',
            website='https://www.studentato-univercity.com/',
            user=user)
db.session.add(portfolio6)

portfolio7 = Portfolio(title='3:56 AM', 
            subtitle='Walk on the moon',
            content="This band's website comes with a gorgeous layout, dark but simple tones with great color nuances that gives the page an edge. The modern feel fits the band images perfectly to create an atmosphere of mystery and elegance.",
            tag=tag2.name,
            client_name='3:56 AM',
            website='https://www.threefiftysixam.com/',
            user=user)
db.session.add(portfolio7)


db.session.commit()
