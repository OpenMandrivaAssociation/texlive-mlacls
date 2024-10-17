Name:		texlive-mlacls
Version:	72271
Release:	1
Summary:	LaTeX class for MLA papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mlacls
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlacls.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlacls.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlacls.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In the United States, secondary and undergraduate students are
generally expected to adhere to the format prescribed by the
Modern Language Association (MLA) for typewritten essays,
research papers and writings. This package provides a simple,
straightforward LaTeX class for composing papers almost
perfectly adherent to the MLA style guide.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mlacls
%{_texmfdistdir}/tex/latex/mlacls
%doc %{_texmfdistdir}/doc/latex/mlacls

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
