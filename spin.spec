Summary:	On-the-fly, LTL model checking with SPIN
Summary(pl):	Sprawdzanie modeli LTL w locie przy u¿yciu SPIN
Name:		spin
Version:	4.1.1
Release:	0.1
License:	Spin Public license
Group:		Development/Tools
Source0:	http://spinroot.com/spin/Src/%{name}411.tar.gz
# Source0-md5:	92cfde0b46dc3a006a4bd55525a8eb1d
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

%description -l pl
Spin to popularne narzêdzie, którego mo¿na u¿ywaæ do formalnego
sprawdzania systemów programów rozproszonych. Narzêdzie by³o rozwijane
w Bell Labs w oryginalnej grupie Uniksa z Computing Sciences Research
Center pocz±wszy od 1980 roku. Jest dostêpne za darmo od 1991 i nadal
dotrzymuje kroku. We wrze¶niu 2002 narzêdzie to otrzyma³o presti¿ow±
nagrodê System Software Award 2001 roku od ACM.

http://cm.bell-labs.com/cm/cs/what/spin/spin_license.html

%package xspin
Summary:	Graphical user interface to Spin
Summary(pl):	Graficzny interfejs u¿ytkownika do Spina
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description xspin
Xspin is graphical user interface to Spin, written in Tcl/Tk.

%description xspin -l pl
Xspin to graficzny interfejs u¿ytkownika do Spina, napisany w Tcl/Tk.

%prep
%setup -q -c

%build
cd Src*
%{__make} -f make_unix \
	CFLAGS="-ansi -D_POSIX_SOURCE %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}

install Src*/spin $RPM_BUILD_ROOT%{_bindir}
install Man/spin.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a Test/* $RPM_BUILD_ROOT%{_datadir}/%{name}

echo "#!/usr/bin/wish -f" > $RPM_BUILD_ROOT%{_bindir}/xspin
tail -n $(expr `cat Xspin*/xspin*.tcl | wc -l` - 3) Xspin*/xspin*.tcl >> $RPM_BUILD_ROOT%{_bindir}/xspin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html Doc/*
%attr(755,root,root) %{_bindir}/spin
%{_mandir}/man1/*
%{_datadir}/%{name}

%files xspin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xspin
