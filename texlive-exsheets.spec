Name:		texlive-exsheets
Epoch:		1
Version:	67300
Release:	1
Summary:	Create exercise sheets and exams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exsheets
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exsheets.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exsheets.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to create exercises or questions
and their corresponding solutions. The questions may be divided
into classes and/or topics and may be printed selectively.
Meta-data to questions can be added and recovered. The
solutions may be printed where they are, or collected and
printed at a later point in the document all together, section-
wise or selectively by ID. The package provides the means to
selectively include questions from an external file, and to
control the style of headings of both questions and solutions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/exsheets
%doc %{_texmfdistdir}/doc/latex/exsheets

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
