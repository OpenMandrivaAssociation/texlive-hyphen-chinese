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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for unaccented transliterated Mandarin Chinese
(pinyin) in T1/EC and UTF-8 encodings. The latter can hyphenate pinyin
with or without tone markers; the former only without.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-chinese:
pinyin loadhyph-zh-latn-pinyin.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-chinese:
\addlanguage{pinyin}{loadhyph-zh-latn-pinyin.tex}{}{1}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-chinese:
['pinyin'] = {
	loader = 'loadhyph-zh-latn-pinyin.tex',
	lefthyphenmin = 1,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-zh-latn-pinyin.pat.txt',
},
TL_HYPHEN_EOF
