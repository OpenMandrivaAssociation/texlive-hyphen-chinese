Name:		texlive-hyphen-chinese
Version:	20111102
Release:	1
Summary:	Chinese pinyin hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-chinese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-hyphen-base

%description
Hyphenation patterns for unaccented transliterated Mandarin
Chinese (pinyin) in T1/EC and UTF-8 encodings.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-chinese
%_texmf_language_def_d/hyphen-chinese
%_texmf_language_lua_d/hyphen-chinese

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-chinese <<EOF
%% from hyphen-chinese:
pinyin loadhyph-zh-latn-pinyin.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-chinese <<EOF
%% from hyphen-chinese:
\addlanguage{pinyin}{loadhyph-zh-latn-pinyin.tex}{}{1}{1}
EOF
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
