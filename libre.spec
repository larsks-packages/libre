Name:           libre
Version:        0.4.4
Release:        5%{?dist}
Summary:        Portable SIP library (runtime)

License:        BSD
URL:            http://www.creytiv.com/re.html
Source0:        http://www.creytiv.com/pub/re-%{version}.tar.gz
Patch100:       libre-0.4.4-lib-version.patch

BuildRequires:  openssl-devel

%description
Libre is a portable and generic library for real-time communications with
async IO support and a complete SIP stack with support for SDP, RTP/RTCP,
STUN/TURN/ICE, BFCP and DNS Client. 

This package contains the runtime libraries necessary to run programs
linked against re.

%package devel
Summary:        Portable SIP library (development)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libre is a portable and generic library for real-time communications with
async IO support and a complete SIP stack with support for SDP, RTP/RTCP,
STUN/TURN/ICE, BFCP and DNS Client. 

This package contains the libraries and header files necessary to compile
code that uses re.


%prep
%setup -q -n re-%{version}
%patch100 -p1 -b.libversion

%build
make %{?_smp_mflags} LIBDIR=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
%make_install LIBDIR=%{_libdir} MKDIR=%{_datadir}/re
ln -s libre.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libre.so
rm -f $RPM_BUILD_ROOT%{_libdir}/libre.a

%files
%doc docs/*

%{_libdir}/libre.so.*

%files devel
%dir %{_includedir}/re/
%{_includedir}/re/*.h
%dir %{_datadir}/re/
%{_datadir}/re/re.mk
%{_libdir}/libre.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog

* Sun Sep 29 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.4-5
- generate a versioned shared library
- removed static library from devel package
- ensure correct ownership of directories

* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.4-1
- initial package

