from dataclasses import dataclass

@dataclass
class blog_post:
    content: str
    timestamp: str
    
new_blog = blog_post("hello world!", "10-10-2026")
print(new_blog)
