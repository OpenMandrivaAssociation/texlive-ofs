# revision 16991
# category Package
# catalog-ctan /macros/generic/ofs
# catalog-date 2010-02-12 21:26:56 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-ofs
Version:	20100212
Release:	10
Summary:	Macros for managing large font collections
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/ofs
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ofs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ofs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
OFS (Olsak's Font System) is a set of Plain TeX and LaTeX
macros for managing large font collections; it has been used by
Czech/Slovak users for many years. Main features include: -
Mapping from long names of fonts to the metric file name. The
user can specify only exact long names in documents. - Support
for many font encodings. - Printing of catalogues of fonts and
test samples of font families; the interactive macro \showfonts
shows all font families you have installed via OFS. - The user
interface is the same for Plain TeX and for LaTeX, but the
implementation differs: the LaTeX variant of OFS uses NFSS, but
the Plain variant implements its own font management (which may
even be better than NFSS) - Support for math fonts including TX
fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ofs/a117.tex
%{_texmfdistdir}/tex/generic/ofs/a35.sty
%{_texmfdistdir}/tex/generic/ofs/a35.tex
%{_texmfdistdir}/tex/generic/ofs/allfonts.sty
%{_texmfdistdir}/tex/generic/ofs/allfonts.tex
%{_texmfdistdir}/tex/generic/ofs/amsfn.tex
%{_texmfdistdir}/tex/generic/ofs/mtfn.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-6a.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-6c.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-6k.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-6s.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-6t.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-6x.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-6y.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-8c.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-8t.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-8x.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-8z.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-ams.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-cm.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-mt.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-ps.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-px.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-slt.tex
%{_texmfdistdir}/tex/generic/ofs/ofs-tx.tex
%{_texmfdistdir}/tex/generic/ofs/ofs.sty
%{_texmfdistdir}/tex/generic/ofs/ofs.tex
%{_texmfdistdir}/tex/generic/ofs/ofsdef.tex
%{_texmfdistdir}/tex/generic/ofs/pantyk.tex
%{_texmfdistdir}/tex/generic/ofs/txfn.tex
%doc %{_texmfdistdir}/doc/generic/ofs/changes.txt
%doc %{_texmfdistdir}/doc/generic/ofs/eurotex2003-ofs.pdf
%doc %{_texmfdistdir}/doc/generic/ofs/eurotex2003-ofs.tex
%doc %{_texmfdistdir}/doc/generic/ofs/ofs-slt.pdf
%doc %{_texmfdistdir}/doc/generic/ofs/ofsdoc-e.pdf
%doc %{_texmfdistdir}/doc/generic/ofs/ofsdoc-e.tex
%doc %{_texmfdistdir}/doc/generic/ofs/ofsdoc.pdf
%doc %{_texmfdistdir}/doc/generic/ofs/ofsdoc.tex
%doc %{_texmfdistdir}/doc/generic/ofs/ofsmtdef.tex
%doc %{_texmfdistdir}/doc/generic/ofs/ofstest.tex
%doc %{_texmfdistdir}/doc/generic/ofs/readme.ofs

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100212-2
+ Revision: 754504
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100212-1
+ Revision: 719154
- texlive-ofs
- texlive-ofs
- texlive-ofs
- texlive-ofs

