# Generated from ruby-openid-2.1.8.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	ruby-openid

Summary:	A library for consuming and serving OpenID identities
Name:		rubygem-%{rbname}

Version:	2.1.8
Release:	1
Group:		Development/Ruby
License:	ASL 2.0
URL:		http://github.com/openid/ruby-openid
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Ruby OpenID is a Ruby library for verifying and serving OpenID identities.
 
==Features
* Easy to use API for verifying OpenID identites - OpenID::Consumer
* Support for serving OpenID identites - OpenID::Server
* Does not depend on underlying web framework
* Supports multiple storage mechanisms (Filesystem, ActiveRecord, Memory)
* Example code to help you get started, including:
  * Ruby on Rails based consumer and server
  * OpenIDLoginGenerator for quickly getting creating a rails app that uses
    OpenID for authentication
  * ActiveRecordOpenIDStore plugin
* Comprehensive test suite
* Supports both OpenID 1 and OpenID 2 transparently

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(admin|examples|test)/'

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/admin
%{ruby_gemdir}/gems/%{rbname}-%{version}/admin/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/INSTALL
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/UPGRADE
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Sun Mar 13 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.1.8-1
+ Revision: 644330
- regenerate spec with gem2rpm5
- new release: 2.1.8

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.7-2mdv2011.0
+ Revision: 614796
- the mass rebuild of 2010.1 packages

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.1.7-1mdv2010.1
+ Revision: 500503
- import rubygem-ruby-openid


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.1.7-1
- initial release
