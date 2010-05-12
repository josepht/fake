Name:       fake
Version:    1.0
Release:    2
Summary:    fake provides/etc
License:    GPL
Group:      System Environment/Base
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%description
fake build deps
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
touch $RPM_BUILD_ROOT/usr/bin/nosuchfile
%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/bin/nosuchfile

