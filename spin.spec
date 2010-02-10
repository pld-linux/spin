Summary:	On-the-fly, LTL model checking with SPIN
Summary(pl.UTF-8):	Sprawdzanie modeli LTL w locie przy użyciu SPIN
Name:		spin
Version:	5.2.4
Release:	1
License:	Spin Public license
Group:		Development/Tools
Source0:	http://spinroot.com/spin/Src/%{name}524.tar.gz
# Source0-md5:	c869e7bd83c70be6565cf77c6a98b72c
Source1:	http://spinroot.com/spin/Src/xspin523.tcl
# Source1-md5:	893eb05798802cea4f281daaf34ce190
URL:		http://spinroot.com/spin/whatispin.html
BuildRequires:	yacc
Requires:	tcl
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spin is a popular software tool that can be used for the formal
verification of distributed software systems. The tool was developed
at Bell Labs in the original Unix group of the Computing Sciences
Research Center, starting in 1980. The software has been available
freely since 1991, and continues to evolve to keep pace with new
developments in the field. In April 2002 the tool was awarded the
prestigious System Software Award for 2001 by the ACM.

http://cm.bell-labs.com/cm/cs/what/spin/spin_license.html

%description -l pl.UTF-8
Spin to popularne narzędzie, którego można używać do formalnego
sprawdzania systemów programów rozproszonych. Narzędzie było rozwijane
w Bell Labs w oryginalnej grupie Uniksa z Computing Sciences Research
Center począwszy od 1980 roku. Jest dostępne za darmo od 1991 i nadal
dotrzymuje kroku. We wrześniu 2002 narzędzie to otrzymało prestiżową
nagrodę System Software Award 2001 roku od ACM.

http://cm.bell-labs.com/cm/cs/what/spin/spin_license.html

%package xspin
Summary:	Graphical user interface to Spin
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do Spina
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description xspin
Xspin is graphical user interface to Spin, written in Tcl/Tk.

%description xspin -l pl.UTF-8
Xspin to graficzny interfejs użytkownika do Spina, napisany w Tcl/Tk.

%prep
%setup -q -c

%build
cd Spin/Src*
%{__make} CFLAGS="-ansi -D_POSIX_SOURCE %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}

install Spin/Src*/spin $RPM_BUILD_ROOT%{_bindir}
install Spin/Man/spin.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a Spin/Test/* $RPM_BUILD_ROOT%{_datadir}/%{name}

echo "#!/usr/bin/wish -f" > $RPM_BUILD_ROOT%{_bindir}/xspin
tail -n $(expr `cat %{SOURCE1} | wc -l` - 3) %{SOURCE1} >> $RPM_BUILD_ROOT%{_bindir}/xspin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Spin/README.html Spin/Doc/*
%attr(755,root,root) %{_bindir}/spin
%{_mandir}/man1/*
%{_datadir}/%{name}

%files xspin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xspin
