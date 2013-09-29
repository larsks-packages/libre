Name:           libre
Version:        0.4.4
Release:        2%{?dist}
Summary:        Portable SIP library (runtime)

License:        BSD
URL:            http://www.creytiv.com/re.html
Source0:        http://www.creytiv.com/pub/re-%{version}.tar.gz

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
%setup -q


%build
make %{?_smp_mflags} LIBDIR=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
%make_install LIBDIR=%{_libdir} MKDIR=%{_datadir}/re


%files
%doc docs/*

%{_libdir}/libre.so

%files devel
%{_includedir}/re/
%{_libdir}/libre.a
%{_datadir}/re/re.mk

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog

* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.4-1
- initial package

