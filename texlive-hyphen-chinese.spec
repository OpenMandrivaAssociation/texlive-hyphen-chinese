Name:		texlive-hyphen-chinese
Version:	74115
Release:	1
Summary:	Chinese pinyin hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-chinese.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for unaccented transliterated Mandarin
Chinese (pinyin) in T1/EC and UTF-8 encodings.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-chinese
%_texmf_language_def_d/hyphen-chinese
%_texmf_language_lua_d/hyphen-chinese
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-chinese <<EOF
\%% from hyphen-chinese:
pinyin loadhyph-zh-latn-pinyin.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-chinese
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-chinese <<EOF
\%% from hyphen-chinese:
\addlanguage{pinyin}{loadhyph-zh-latn-pinyin.tex}{}{1}{1}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-chinese
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-chinese <<EOF
-- from hyphen-chinese:
	['pinyin'] = {
		loader = 'loadhyph-zh-latn-pinyin.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-zh-latn-pinyin.pat.txt',
		hyphenation = '',
	},
EOF
