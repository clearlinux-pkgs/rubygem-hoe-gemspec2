#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hoe-gemspec2
Version  : 1.2.0
Release  : 3
URL      : https://rubygems.org/downloads/hoe-gemspec2-1.2.0.gem
Source0  : https://rubygems.org/downloads/hoe-gemspec2-1.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-hoe-doofus
BuildRequires : rubygem-hoe-git
BuildRequires : rubygem-rdoc

%description
= hoe-gemspec2
http://rubygems.org/gems/hoe-gemspec2
{Project}[http://rubygems.org/gems/hoe-gemspec2]
{Documentation}[http://rubydoc.info/github/raggi/hoe-gemspec2]
{Wiki}[http://wiki.github.com/raggi/hoe-gemspec2/]
{Source Code}[http://github.com/raggi/hoe-gemspec2/]
{Issues}[http://github.com/raggi/hoe-gemspec2/issues]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hoe-gemspec2-1.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-hoe-gemspec2.gemspec

%build
gem build rubygem-hoe-gemspec2.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hoe-gemspec2-1.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/hoe-gemspec2-1.2.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/hoe-gemspec2-1.2.0/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/hoe-gemspec2-1.2.0/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/hoe-gemspec2-1.2.0/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/hoe-gemspec2-1.2.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/hoe-gemspec2-1.2.0/lib/hoe/gemspec2.rb
/usr/lib64/ruby/gems/2.3.0/specifications/hoe-gemspec2-1.2.0.gemspec
