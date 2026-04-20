\ProvidesClass{resume}[03/22/2026 v9.1 Ankur's Resume Class]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClass{article}

\usepackage[parfill]{parskip}

\usepackage{array}
\usepackage{ifthen}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{geometry} % Required for adjusting page dimensions and margins
\usepackage{fontspec}
\usepackage{hyperref}

\setmainfont[
  UprightFont    = cmunrm.otf,
  ItalicFont     = cmunti.otf,
  BoldFont       = cmunbx.otf,
  BoldItalicFont = cmunbi.otf
]{CMU Serif}

\pagestyle{empty}

\geometry{
	top=0.45in, % Top margin
	bottom=0.45in, % Bottom margin
	left=0.4in, % Left margin
	right=0.4in, % Right margin
	% showframe, % Uncomment to show how the type block is set on the page
}

\newcommand{\name}[1]{\def\@name{#1}}
\newcommand{\contact}[1]{\def\@contact{#1}}

\newcommand{\printname}{
	\begingroup
		\begin{center}
			{{\fontsize{24pt}{26pt}\selectfont\@name}}
		\end{center}
	\endgroup
}

\newcommand{\printcontact}{
	\begin{center}
		\def \\ {\hspace{0.3em}|\hspace{0.7em}}
		{\fontsize{11pt}{13pt}\selectfont\@contact}
	\end{center}
}

% Print name and contact at the top of the document automatically
\let\ori@document=\document % Store the original \document command
\renewcommand{\document}{%
	\ori@document
	\printname
	\printcontact
}

% Defines the rSection environment for the major sections within the resume
\newenvironment{rSection}[2]{ % 2 Parameters: First letter, Section Title
	\MakeUppercase{
		\fontsize{12pt}{14pt}\selectfont #1
	}
	\hspace{-1.4em}
	\MakeUppercase{
		\fontsize{12pt}{14pt}\selectfont #2
	}
	\vspace{0.5em}
	\hrule
	\begin{list}{}{
		\setlength{\leftmargin}{1em}
	}
	\item[]
}{
	\end{list}
}

\newenvironment{rSectionEntry}[5]{ % 5 parameters: name, dates, tagline, technologies, location
    % --- LINE 1: Name | Tech | Dates ---
    \textbf{\fontsize{11pt}{13pt}\selectfont #1}
    \ifthenelse{\equal{#4}{}}{}{ % If Tech (#4) exists
        \textbf{\hspace{-0.4em}|}\hspace{0em}
\textit{#4}
    }
    \hfill {#2}% <--- Percent prevents trailing space
	\vspace{0.08em}
    \\
    % --- LINE 2: Tagline | Location ---
    \ifthenelse{\equal{#3}{}\and\equal{#5}{}}{
        \vspace{-1.4em}
    }{
		#3% <--- Percent prevents space after tagline
        \hfill
        #5% <--- CRITICAL: Percent prevents trailing space, forcing strict right alignment
    }
    % --- BULLET LIST ---
    \begin{list}{$\bullet\hspace{0.2em}$}{\leftmargin=2.5em}
        \fontsize{10pt}{12pt}\selectfont
        \setlength{\itemsep}{-0.5em}
        \vspace{-0.5em}
}{
    \end{list}
	\vspace{-0.35em}
}

\newenvironment{rSet}[2] % 2 Parameters: title, items
{
    \noindent
    {\fontsize{11pt}{13pt}\selectfont \textbf{#1}}
    \dotfill
    {\fontsize{11pt}{13pt}\selectfont #2}
    \par            % Forces a clean line break
    \vspace{-0.5em} % Pulls the next line up. Adjust this value (e.g., -0.5em) to tighten further.
}{
}