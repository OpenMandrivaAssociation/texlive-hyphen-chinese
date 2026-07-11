%global tl_name hyphen-chinese
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Chinese pinyin hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-chinese
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-chinese.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for unaccented transliterated Mandarin Chinese
(pinyin) in T1/EC and UTF-8 encodings. The latter can hyphenate pinyin
with or without tone markers; the former only without.

