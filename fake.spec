Name:       fake
Version:    1.1
Release:    8.largefile
Summary:    fake package
License:    GPL
Group:      System Environment/Base
Epoch:      7
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
%description
fake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
touch $RPM_BUILD_ROOT/usr/bin/nosuchfile
dd if=/dev/zero of=$RPM_BUILD_ROOT/usr/bin/nosuchfile bs=1M count=5000

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/bin/nosuchfile

