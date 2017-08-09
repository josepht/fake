Name:       fake
Version:    1.1
Release:    9999
Summary:    fake package
License:    GPL
Group:      System Environment/Base
Epoch:      7
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  i386 i686 x86_64
%description
fake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
touch $RPM_BUILD_ROOT/usr/bin/nosuchfile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/bin/nosuchfile

