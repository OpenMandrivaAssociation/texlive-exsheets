%global tl_name exsheets
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.21k
Release:	%{tl_revision}.1
Summary:	Create exercise sheets and exams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exsheets
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exsheets.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exsheets.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to create exercises or questions and
their corresponding solutions. The questions may be divided into classes
and/or topics and may be printed selectively. Meta-data to questions can
be added and recovered. The solutions may be printed where they are, or
collected and printed at a later point in the document all together,
section-wise or selectively by ID. The package provides the means to
selectively include questions from an external file, and to control the
style of headings of both questions and solutions. As of May 2017, this
package has been superseded by its official successor xsim. exsheets
itself is now considered obsolete, but will stay alive, and will
continue to receive bugfix releases. However, new features will not be
added any more.

