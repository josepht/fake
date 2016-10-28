Name:       fake1
Version:    1.0
Release:    24.brew794
Summary:    fake provides/etc
License:    GPL
Group:      System Environment/Base
Epoch:      7
#Source:     junk.dat
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch:  noarch x86_64
BuildArch:      noarch
#ExclusiveArch:  i686
#ExcludeArch:    ppc64le aarch64
#BuildRequires:  tog-pegasus-devel >= 2:2.5.1
Requires:   nosuchpackage > 8192
Prefix:     /usr
Prefix:     /var
%description
fake build deps

%package -n fake
Summary: test
Version: 1.0
Release: 23

%description -n fake
test

%prep
%if 0%{?__nosuchmacro} == 23
echo XXX
%endif
%build
#sleep $(( RANDOM / 500 ))
#exit 1
ulimit -a || :
cat /proc/sys/fs/file-nr || :
#lsof |wc -l || :
echo _unitdir macro is: %{_unitdir}
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
touch $RPM_BUILD_ROOT/usr/bin/nosuchfile
#dd if=/dev/zero of=$RPM_BUILD_ROOT/usr/bin/nosuchfile bs=1M count=2050
#mkdir -p $RPM_BUILD_ROOT/var/fake
#cp $RPM_SOURCE_DIR/junk.dat $RPM_BUILD_ROOT/var/fake
%clean
rm -rf $RPM_BUILD_ROOT
%files -n fake
%defattr(-,bin,bin)
/usr/bin/nosuchfile
#/var/fake/junk.dat

