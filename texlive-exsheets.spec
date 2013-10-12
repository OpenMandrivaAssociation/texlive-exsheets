# revision 31218
# category Package
# catalog-ctan /macros/latex/contrib/exsheets
# catalog-date 2013-07-17 14:16:32 +0200
# catalog-license lppl1.3
# catalog-version 0.9i
Name:		texlive-exsheets
Version:	0.9i
Release:	1
Summary:	Create exercise sheets and exams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exsheets
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exsheets.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exsheets.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/exsheets/cntformats.sty
%{_texmfdistdir}/tex/latex/exsheets/exsheets.sty
%{_texmfdistdir}/tex/latex/exsheets/exsheets_configurations.cfg
%{_texmfdistdir}/tex/latex/exsheets/exsheets_headings.cfg
%{_texmfdistdir}/tex/latex/exsheets/exsheets_headings.def
%{_texmfdistdir}/tex/latex/exsheets/tasks.cfg
%{_texmfdistdir}/tex/latex/exsheets/tasks.sty
%doc %{_texmfdistdir}/doc/latex/exsheets/README
%doc %{_texmfdistdir}/doc/latex/exsheets/cntformats_en.pdf
%doc %{_texmfdistdir}/doc/latex/exsheets/cntformats_en.tex
%doc %{_texmfdistdir}/doc/latex/exsheets/exsheets_en.pdf
%doc %{_texmfdistdir}/doc/latex/exsheets/exsheets_en.tex
%doc %{_texmfdistdir}/doc/latex/exsheets/grading-table.pdf
%doc %{_texmfdistdir}/doc/latex/exsheets/grading-table.tex
%doc %{_texmfdistdir}/doc/latex/exsheets/tasks_en.pdf
%doc %{_texmfdistdir}/doc/latex/exsheets/tasks_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
