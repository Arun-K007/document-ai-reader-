from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

pdf_path = "sample.pdf"

document = SimpleDocTemplate(
    pdf_path,
    pagesize=A4
)

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph("Java Programming - Basic Concepts", styles["Title"])
)

content.append(Spacer(1, 20))

content.append(
    Paragraph(
        "Java is a high-level, object-oriented programming language. "
        "It is widely used to build desktop applications, web applications, "
        "mobile applications, and enterprise software.",
        styles["BodyText"]
    )
)

content.append(Spacer(1, 15))

content.append(
    Paragraph("Inheritance", styles["Heading2"])
)

content.append(
    Paragraph(
        "Java supports inheritance. The extends keyword is used to create "
        "an inheritance relationship between classes. In inheritance, a "
        "child class can acquire properties and methods from a parent class.",
        styles["BodyText"]
    )
)

content.append(Spacer(1, 15))

content.append(
    Paragraph("Encapsulation", styles["Heading2"])
)

content.append(
    Paragraph(
        "Encapsulation is the process of wrapping data and methods together "
        "inside a class. The private keyword can be used to restrict direct "
        "access to variables from outside the class.",
        styles["BodyText"]
    )
)

content.append(Spacer(1, 15))

content.append(
    Paragraph("Polymorphism", styles["Heading2"])
)

content.append(
    Paragraph(
        "Polymorphism allows an object to take multiple forms. It is commonly "
        "implemented through method overloading and method overriding.",
        styles["BodyText"]
    )
)

content.append(Spacer(1, 15))

content.append(
    Paragraph("Method Overriding", styles["Heading2"])
)

content.append(
    Paragraph(
        "Method overriding occurs when a subclass provides its own "
        "implementation of a method inherited from its parent class. "
        "The @Override annotation is commonly used to indicate that "
        "a method is being overridden.",
        styles["BodyText"]
    )
)

content.append(Spacer(1, 15))

content.append(
    Paragraph("Abstraction", styles["Heading2"])
)

content.append(
    Paragraph(
        "Abstraction focuses on hiding implementation details and showing "
        "only the essential functionality to the user. In Java, abstraction "
        "can be implemented using abstract classes and interfaces.",
        styles["BodyText"]
    )
)

content.append(Spacer(1, 15))

content.append(
    Paragraph("Important Java Keywords", styles["Heading2"])
)

keywords = [
    "extends - used for class inheritance.",
    "private - restricts direct access to a class member.",
    "implements - used when a class implements an interface.",
    "this - refers to the current object.",
    "super - refers to the parent class."
]

for keyword in keywords:
    content.append(
        Paragraph(keyword, styles["BodyText"])
    )
    content.append(Spacer(1, 5))

document.build(content)

print("sample.pdf created successfully!")