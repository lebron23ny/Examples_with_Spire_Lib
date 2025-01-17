from spire.doc import *
latexMathCode = \
    [
        "x^{2}+\\sqrt{x^{2}+1}=2",
        "\\cos (2\\theta) = \\cos^2 \\theta - \\sin^2 \\theta",
        "k_{n+1} = n^2 + k_n^2 - k_{n-1}",
        "\\frac {\\frac {1}{x}+ \\frac {1}{y}}{y-z}",
        "\\int_0^ \\infty \\mathrm {e}^{-x} \\, \\mathrm {d}x",
        "\\forall x \\in X, \\quad \\exists y \\leq \\epsilon",
        "\\alpha, \\beta, \\gamma, \\Gamma, \\pi, \\Pi, \\phi, \\varphi, \\mu, \\Phi",
        "A_{m,n} = \\begin{pmatrix} a_{1,1} & a_{1,2} & \\cdots & a_{1,n} \\\\ a_{2,1} & a_{2,2} & \\cdots & a_{2,n} \\\\ \\vdots  & \\vdots  & \\ddots & \\vdots  \\\\ a_{m,1} & a_{m,2} & \\cdots & a_{m,n} \\end{pmatrix}",
    ]
mathMLCode =\
    [
        "<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>a</mi><mo>≠</mo><mn>0</mn></math>",
        "<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>",
        "<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>x</mi><mo>=</mo><mrow><mfrac><mrow><mo>−</mo><mi>b</mi><mo>±</mo><msqrt><msup><mi>b</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mi>a</mi><mi>c</mi></msqrt></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></mrow></math>",
    ]

doc = Document()
section = doc.AddSection()
textPara = section.AddParagraph()
textPara.AppendText("Creating Equations from LaTeX Code")
textPara.ApplyStyle(BuiltinStyle.Heading1)
textPara.Format.HorizontalAlignment = HorizontalAlignment.Center

for f in latexMathCode:
    officeMath = OfficeMath(doc)
    officeMath.FromLatexMathCode(f)

    paragraph = section.AddParagraph()
    paragraph.Items.Add(officeMath)
    section.AddParagraph()

section.AddParagraph()

textPara = section.AddParagraph()
textPara.AppendText("Creating Equations from MathML Code")
textPara.ApplyStyle(BuiltinStyle.Heading1)
textPara.Format.HorizontalAlignment = HorizontalAlignment.Center

for f in mathMLCode:
    officeMath = OfficeMath(doc)
    officeMath.FromMathMLCode(f)
    paragraph = section.AddParagraph()
    paragraph.Items.Add(officeMath)
    section.AddParagraph()

doc.SaveToFile("AddMathEquations.docx", FileFormat.Docx2013)
doc.Dispose()
