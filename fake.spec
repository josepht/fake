Name:       fake
Version:    1.0
Release:    23
Summary:    fake provides/etc
License:    GPL
Group:      System Environment/Base
Epoch:      7
#Source:     junk.dat
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch:  noarch x86_64
BuildArch:          noarch
BuildArchitectures: x86_64
ExcludeArch:        ppc ppc64 s390 s390x
Requires:   nosuchpackage > 8192
Prefix:     /usr
Prefix:     /var
%description
fake build deps
%prep
%if 0%{?__nosuchmacro} == 23
echo XXX
%endif
%build
#sleep $(( RANDOM / 500 ))
#exit 1
ulimit -a || :
cat /proc/sys/fs/file-nr || :
lsof |wc -l || :
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
%files
/usr/bin/nosuchfile
#/var/fake/junk.dat

