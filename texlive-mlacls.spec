%global tl_name mlacls
%global tl_revision 72271

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	LaTeX class for MLA papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mlacls
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mlacls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mlacls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mlacls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In the United States, secondary and undergraduate students are generally
expected to adhere to the format prescribed by the Modern Language
Association (MLA) for typewritten essays, research papers and writings.
This package provides a simple, straightforward LaTeX class for
composing papers almost perfectly adherent to the MLA style guide.

